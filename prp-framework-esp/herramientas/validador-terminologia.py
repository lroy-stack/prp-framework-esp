#!/usr/bin/env python3
"""
Validador de Terminología PRP Framework
Herramienta para validar consistencia terminológica en traducciones.

Uso:
    python validador-terminologia.py --archivo README-es.md --glosario ../configuracion/glosario-maestro.json
    python validador-terminologia.py --directorio ../repositorios/context-engineering-intro-esp/
    python validador-terminologia.py --verificar-todo
"""

import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class TerminoValidacion:
    """Resultado de validación de un término"""
    termino: str
    archivo: str
    linea: int
    contexto: str
    tipo_error: str
    sugerencia: str

@dataclass
class ResultadoValidacion:
    """Resultado completo de validación"""
    archivos_procesados: int
    errores_encontrados: List[TerminoValidacion]
    terminos_verificados: int
    consistencia_porcentaje: float

class ValidadorTerminologia:
    """Validador de terminología para traducciones PRP Framework"""
    
    def __init__(self, ruta_glosario: Path):
        self.glosario = self._cargar_glosario(ruta_glosario)
        self.patrones_terminos = self._compilar_patrones()
        
    def _cargar_glosario(self, ruta: Path) -> Dict:
        """Carga el glosario maestro"""
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Glosario no encontrado: {ruta}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error JSON en glosario: {e}")
            raise
    
    def _compilar_patrones(self) -> Dict[str, re.Pattern]:
        """Compila patrones regex para términos del glosario"""
        patrones = {}
        
        # Compilar patrones para todas las categorías
        for categoria in ['terminos_core', 'terminos_metodologia', 'terminos_tecnicos', 
                         'terminos_herramientas', 'terminos_ui']:
            if categoria in self.glosario:
                for termino, info in self.glosario[categoria].items():
                    # Patrón que busca el término original en contextos donde debería estar traducido
                    if not info.get('mantener_original', False):
                        patron = re.compile(
                            r'\b' + re.escape(termino) + r'\b',
                            re.IGNORECASE
                        )
                        patrones[termino] = {
                            'patron': patron,
                            'traduccion': info['traduccion'],
                            'mantener_original': info.get('mantener_original', False),
                            'categoria': info['categoria']
                        }
        
        return patrones
    
    def validar_archivo(self, ruta_archivo: Path) -> List[TerminoValidacion]:
        """Valida terminología en un archivo específico"""
        errores = []
        
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
        except UnicodeDecodeError:
            logger.warning(f"No se pudo leer archivo (encoding): {ruta_archivo}")
            return errores
        except Exception as e:
            logger.error(f"Error leyendo archivo {ruta_archivo}: {e}")
            return errores
        
        for num_linea, linea in enumerate(lineas, 1):
            # Saltar líneas de código (entre ``` o con espacios iniciales)
            if self._es_linea_codigo(linea, lineas, num_linea - 1):
                continue
                
            errores.extend(self._validar_linea(linea, ruta_archivo, num_linea))
        
        return errores
    
    def _es_linea_codigo(self, linea: str, todas_lineas: List[str], indice: int) -> bool:
        """Determina si una línea es código y debe saltarse"""
        # Líneas que empiezan con espacios (código indentado)
        if linea.startswith('    ') or linea.startswith('\\t'):
            return True
        
        # Líneas dentro de bloques de código ```
        en_bloque_codigo = False
        for i in range(indice):
            if '```' in todas_lineas[i]:
                en_bloque_codigo = not en_bloque_codigo
        
        return en_bloque_codigo
    
    def _validar_linea(self, linea: str, archivo: Path, num_linea: int) -> List[TerminoValidacion]:
        """Valida terminología en una línea específica"""
        errores = []
        
        for termino, info in self.patrones_terminos.items():
            coincidencias = info['patron'].finditer(linea)
            
            for coincidencia in coincidencias:
                # Si el término NO debe mantener original y aparece en inglés
                if not info['mantener_original']:
                    contexto = self._extraer_contexto(linea, coincidencia.start(), coincidencia.end())
                    
                    error = TerminoValidacion(
                        termino=termino,
                        archivo=str(archivo),
                        linea=num_linea,
                        contexto=contexto,
                        tipo_error="termino_no_traducido",
                        sugerencia=f"Usar '{info['traduccion']}' en lugar de '{termino}'"
                    )
                    errores.append(error)
        
        return errores
    
    def _extraer_contexto(self, linea: str, inicio: int, fin: int, ventana: int = 20) -> str:
        """Extrae contexto alrededor del término encontrado"""
        inicio_contexto = max(0, inicio - ventana)
        fin_contexto = min(len(linea), fin + ventana)
        
        contexto = linea[inicio_contexto:fin_contexto].strip()
        
        # Marcar el término problemático
        termino_marcado = f">>>{linea[inicio:fin]}<<<\\"
        contexto = contexto.replace(linea[inicio:fin], termino_marcado)
        
        return contexto
    
    def validar_directorio(self, ruta_directorio: Path, extensiones: Set[str] = {'.md', '.txt'}) -> ResultadoValidacion:
        """Valida terminología en todos los archivos de un directorio"""
        errores_totales = []
        archivos_procesados = 0
        
        for archivo in ruta_directorio.rglob('*'):
            if archivo.is_file() and archivo.suffix.lower() in extensiones:
                logger.info(f"Validando: {archivo}")
                errores = self.validar_archivo(archivo)
                errores_totales.extend(errores)
                archivos_procesados += 1
        
        # Calcular métricas
        terminos_verificados = len(self.patrones_terminos) * archivos_procesados
        consistencia = max(0, 100 - (len(errores_totales) / max(1, terminos_verificados) * 100))
        
        return ResultadoValidacion(
            archivos_procesados=archivos_procesados,
            errores_encontrados=errores_totales,
            terminos_verificados=terminos_verificados,
            consistencia_porcentaje=consistencia
        )
    
    def generar_reporte(self, resultado: ResultadoValidacion, ruta_salida: Path = None) -> str:
        """Genera reporte de validación"""
        reporte = [
            "# 📊 REPORTE DE VALIDACIÓN TERMINOLÓGICA\\n",
            f"**Archivos procesados**: {resultado.archivos_procesados}",
            f"**Términos verificados**: {resultado.terminos_verificados}",
            f"**Errores encontrados**: {len(resultado.errores_encontrados)}",
            f"**Consistencia**: {resultado.consistencia_porcentaje:.1f}%\\n"
        ]
        
        if resultado.errores_encontrados:
            reporte.append("## 🚨 Errores Encontrados\\n")
            
            # Agrupar errores por archivo
            errores_por_archivo = {}
            for error in resultado.errores_encontrados:
                archivo = Path(error.archivo).name
                if archivo not in errores_por_archivo:
                    errores_por_archivo[archivo] = []
                errores_por_archivo[archivo].append(error)
            
            for archivo, errores in errores_por_archivo.items():
                reporte.append(f"### 📄 {archivo}\\n")
                for error in errores:
                    reporte.extend([
                        f"**Línea {error.linea}**: {error.termino}",
                        f"- *Contexto*: {error.contexto}",
                        f"- *Sugerencia*: {error.sugerencia}\\n"
                    ])
        else:
            reporte.append("## ✅ ¡Sin errores encontrados!\\n")
            reporte.append("La terminología es consistente con el glosario maestro.")
        
        contenido_reporte = "\\n".join(reporte)
        
        if ruta_salida:
            with open(ruta_salida, 'w', encoding='utf-8') as f:
                f.write(contenido_reporte)
            logger.info(f"Reporte guardado en: {ruta_salida}")
        
        return contenido_reporte
    
    def obtener_estadisticas_glosario(self) -> Dict:
        """Obtiene estadísticas del glosario cargado"""
        stats = {
            'total_terminos': 0,
            'por_categoria': {},
            'mantener_original': 0,
            'traducir': 0
        }
        
        for categoria in ['terminos_core', 'terminos_metodologia', 'terminos_tecnicos', 
                         'terminos_herramientas', 'terminos_ui']:
            if categoria in self.glosario:
                count = len(self.glosario[categoria])
                stats['por_categoria'][categoria] = count
                stats['total_terminos'] += count
                
                # Contar términos que mantienen original vs traducir
                for info in self.glosario[categoria].values():
                    if info.get('mantener_original', False):
                        stats['mantener_original'] += 1
                    else:
                        stats['traducir'] += 1
        
        return stats

def main():
    parser = argparse.ArgumentParser(description='Validador de Terminología PRP Framework')
    parser.add_argument('--archivo', type=Path, help='Archivo específico a validar')
    parser.add_argument('--directorio', type=Path, help='Directorio a validar recursivamente')
    parser.add_argument('--verificar-todo', action='store_true', help='Verificar todos los repositorios')
    parser.add_argument('--glosario', type=Path, 
                       default=Path(__file__).parent.parent / 'configuracion' / 'glosario-maestro.json',
                       help='Ruta al glosario maestro')
    parser.add_argument('--reporte', type=Path, help='Guardar reporte en archivo')
    parser.add_argument('--estadisticas', action='store_true', help='Mostrar estadísticas del glosario')
    
    args = parser.parse_args()
    
    try:
        validador = ValidadorTerminologia(args.glosario)
        
        if args.estadisticas:
            stats = validador.obtener_estadisticas_glosario()
            print("\\n📊 ESTADÍSTICAS DEL GLOSARIO")
            print(f"Total términos: {stats['total_terminos']}")
            print(f"Mantener original: {stats['mantener_original']}")
            print(f"Traducir: {stats['traducir']}")
            print("\\nPor categoría:")
            for cat, count in stats['por_categoria'].items():
                print(f"  {cat}: {count}")
            return
        
        if args.archivo:
            logger.info(f"Validando archivo: {args.archivo}")
            errores = validador.validar_archivo(args.archivo)
            resultado = ResultadoValidacion(1, errores, len(validador.patrones_terminos), 
                                          max(0, 100 - len(errores)))
            
        elif args.directorio:
            logger.info(f"Validando directorio: {args.directorio}")
            resultado = validador.validar_directorio(args.directorio)
            
        elif args.verificar_todo:
            # Validar todos los repositorios
            base_dir = Path(__file__).parent.parent / 'repositorios'
            logger.info(f"Validando todos los repositorios en: {base_dir}")
            resultado = validador.validar_directorio(base_dir)
            
        else:
            parser.print_help()
            return
        
        # Generar y mostrar reporte
        reporte = validador.generar_reporte(resultado, args.reporte)
        print(reporte)
        
        # Exit code basado en errores encontrados
        exit_code = 1 if resultado.errores_encontrados else 0
        logger.info(f"Validación completada con código: {exit_code}")
        return exit_code
        
    except Exception as e:
        logger.error(f"Error durante validación: {e}")
        return 1

if __name__ == "__main__":
    exit(main())