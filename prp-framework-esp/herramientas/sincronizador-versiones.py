#!/usr/bin/env python3
"""
Sincronizador de Versiones PRP Framework
Herramienta para sincronizar repositorios originales con sistema de traducción.

Uso:
    python sincronizador-versiones.py --update
    python sincronizador-versiones.py --status
    python sincronizador-versiones.py --comparar README.md README-es.md
"""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class VersionInfo:
    """Información de versión de un archivo"""
    archivo: str
    ruta_completa: str
    fecha_modificacion: datetime
    tamaño: int
    hash_contenido: str
    estado: str  # 'nuevo', 'modificado', 'sin_cambios'

@dataclass
class SincronizacionResult:
    """Resultado de sincronización"""
    archivos_nuevos: List[str]
    archivos_modificados: List[str]
    archivos_eliminados: List[str]
    errores: List[str]
    tiempo_ejecucion: float

class SincronizadorVersiones:
    """Sincronizador de versiones para repositorios PRP Framework"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.config_dir = self.base_dir / 'configuracion'
        self.repos_dir = self.base_dir / 'repositorios'
        self.metadatos_dir = self.base_dir / 'metadatos'
        
        # Cargar configuración
        self.mapeo_archivos = self._cargar_mapeo_archivos()
        self.estado_general = self._cargar_estado_general()
        
    def _cargar_mapeo_archivos(self) -> Dict:
        """Carga configuración de mapeo de archivos"""
        try:
            mapeo_path = self.config_dir / 'mapeo-archivos.json'
            with open(mapeo_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Archivo de mapeo no encontrado: {mapeo_path}")
            return {}
    
    def _cargar_estado_general(self) -> Dict:
        """Carga estado general del sistema"""
        try:
            estado_path = self.metadatos_dir / 'estado-general.json'
            with open(estado_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Estado general no encontrado, inicializando nuevo")
            return self._inicializar_estado_general()
    
    def _inicializar_estado_general(self) -> Dict:
        """Inicializa estado general por defecto"""
        return {
            "metadatos": {
                "version": "1.0.0",
                "fecha_creacion": datetime.now().isoformat(),
                "ultima_actualizacion": datetime.now().isoformat()
            },
            "frameworks": {},
            "estadisticas_globales": {
                "archivos_identificados": 0,
                "archivos_traducidos": 0,
                "ultima_sincronizacion": None
            }
        }
    
    def _calcular_hash_archivo(self, ruta_archivo: Path) -> str:
        """Calcula hash del contenido de un archivo"""
        try:
            import hashlib
            with open(ruta_archivo, 'rb') as f:
                contenido = f.read()
                return hashlib.md5(contenido).hexdigest()
        except Exception as e:
            logger.error(f"Error calculando hash para {ruta_archivo}: {e}")
            return ""
    
    def _obtener_info_archivo(self, ruta_archivo: Path) -> VersionInfo:
        """Obtiene información completa de un archivo"""
        try:
            stat = ruta_archivo.stat()
            return VersionInfo(
                archivo=ruta_archivo.name,
                ruta_completa=str(ruta_archivo),
                fecha_modificacion=datetime.fromtimestamp(stat.st_mtime),
                tamaño=stat.st_size,
                hash_contenido=self._calcular_hash_archivo(ruta_archivo),
                estado='sin_cambios'
            )
        except Exception as e:
            logger.error(f"Error obteniendo info de {ruta_archivo}: {e}")
            return None
    
    def escanear_repositorio_original(self, framework: str) -> List[VersionInfo]:
        """Escanea un repositorio original para detectar archivos"""
        framework_config = self.mapeo_archivos.get('frameworks', {}).get(framework, {})
        directorio_original = framework_config.get('directorio_original', '')
        
        if not directorio_original:
            logger.error(f"Directorio original no configurado para {framework}")
            return []
        
        # Construir ruta absoluta
        ruta_original = self.base_dir.parent / directorio_original.lstrip('../')
        
        if not ruta_original.exists():
            logger.error(f"Directorio original no existe: {ruta_original}")
            return []
        
        archivos_info = []
        
        # Escanear archivos .md principalmente
        for archivo_md in ruta_original.rglob('*.md'):
            # Saltar directorios específicos
            if any(excluir in str(archivo_md) for excluir in ['.git', 'node_modules', '__pycache__']):
                continue
                
            info = self._obtener_info_archivo(archivo_md)
            if info:
                archivos_info.append(info)
        
        # Incluir archivos específicos mencionados en configuración
        archivos_criticos = framework_config.get('archivos_criticos', {})
        for archivo_critico in archivos_criticos.keys():
            ruta_critica = ruta_original / archivo_critico
            if ruta_critica.exists():
                info = self._obtener_info_archivo(ruta_critica)
                if info and info not in archivos_info:
                    archivos_info.append(info)
        
        logger.info(f"Escaneados {len(archivos_info)} archivos en {framework}")
        return archivos_info
    
    def sincronizar_framework(self, framework: str) -> SincronizacionResult:
        """Sincroniza un framework específico"""
        inicio = datetime.now()
        resultado = SincronizacionResult([], [], [], [], 0.0)
        
        try:
            # Escanear archivos originales
            archivos_originales = self.escanear_repositorio_original(framework)
            
            if not archivos_originales:
                resultado.errores.append(f"No se encontraron archivos para {framework}")
                return resultado
            
            # Comparar con estado anterior si existe
            estado_framework = self.estado_general.get('frameworks', {}).get(framework, {})
            archivos_anteriores = estado_framework.get('archivos_sincronizados', {})
            
            for archivo_info in archivos_originales:
                archivo_anterior = archivos_anteriores.get(archivo_info.archivo, {})
                hash_anterior = archivo_anterior.get('hash_contenido', '')
                
                if not hash_anterior:
                    # Archivo nuevo
                    resultado.archivos_nuevos.append(archivo_info.archivo)
                    archivo_info.estado = 'nuevo'
                elif hash_anterior != archivo_info.hash_contenido:
                    # Archivo modificado
                    resultado.archivos_modificados.append(archivo_info.archivo)
                    archivo_info.estado = 'modificado'
                else:
                    # Sin cambios
                    archivo_info.estado = 'sin_cambios'
            
            # Detectar archivos eliminados
            for archivo_anterior in archivos_anteriores.keys():
                if archivo_anterior not in [a.archivo for a in archivos_originales]:
                    resultado.archivos_eliminados.append(archivo_anterior)
            
            # Actualizar estado
            self._actualizar_estado_framework(framework, archivos_originales)
            
        except Exception as e:
            logger.error(f"Error sincronizando {framework}: {e}")
            resultado.errores.append(str(e))
        
        resultado.tiempo_ejecucion = (datetime.now() - inicio).total_seconds()
        return resultado
    
    def _actualizar_estado_framework(self, framework: str, archivos: List[VersionInfo]):
        """Actualiza el estado de un framework en metadatos"""
        if 'frameworks' not in self.estado_general:
            self.estado_general['frameworks'] = {}
        
        if framework not in self.estado_general['frameworks']:
            self.estado_general['frameworks'][framework] = {}
        
        # Actualizar información de archivos
        archivos_sincronizados = {}
        for archivo in archivos:
            archivos_sincronizados[archivo.archivo] = {
                'ruta_completa': archivo.ruta_completa,
                'fecha_modificacion': archivo.fecha_modificacion.isoformat(),
                'tamaño': archivo.tamaño,
                'hash_contenido': archivo.hash_contenido,
                'estado': archivo.estado
            }
        
        self.estado_general['frameworks'][framework]['archivos_sincronizados'] = archivos_sincronizados
        self.estado_general['frameworks'][framework]['ultima_sincronizacion'] = datetime.now().isoformat()
        
        # Actualizar estadísticas globales
        total_archivos = sum(len(fw.get('archivos_sincronizados', {})) 
                           for fw in self.estado_general['frameworks'].values())
        self.estado_general['estadisticas_globales']['archivos_identificados'] = total_archivos
        self.estado_general['estadisticas_globales']['ultima_sincronizacion'] = datetime.now().isoformat()
    
    def sincronizar_todo(self) -> Dict[str, SincronizacionResult]:
        """Sincroniza todos los frameworks"""
        frameworks = list(self.mapeo_archivos.get('frameworks', {}).keys())
        resultados = {}
        
        logger.info(f"Iniciando sincronización de {len(frameworks)} frameworks...")
        
        for framework in frameworks:
            logger.info(f"Sincronizando {framework}...")
            resultado = self.sincronizar_framework(framework)
            resultados[framework] = resultado
            
            # Log resultados
            if resultado.archivos_nuevos:
                logger.info(f"  Nuevos: {len(resultado.archivos_nuevos)}")
            if resultado.archivos_modificados:
                logger.info(f"  Modificados: {len(resultado.archivos_modificados)}")
            if resultado.errores:
                logger.warning(f"  Errores: {len(resultado.errores)}")
        
        # Guardar estado actualizado
        self._guardar_estado_general()
        
        return resultados
    
    def _guardar_estado_general(self):
        """Guarda el estado general actualizado"""
        try:
            estado_path = self.metadatos_dir / 'estado-general.json'
            with open(estado_path, 'w', encoding='utf-8') as f:
                json.dump(self.estado_general, f, indent=2, ensure_ascii=False)
            logger.info(f"Estado general guardado en {estado_path}")
        except Exception as e:
            logger.error(f"Error guardando estado general: {e}")
    
    def obtener_status(self) -> Dict:
        """Obtiene status actual del sistema"""
        status = {
            'fecha_consulta': datetime.now().isoformat(),
            'frameworks': {},
            'resumen': {
                'total_frameworks': 0,
                'total_archivos': 0,
                'archivos_nuevos': 0,
                'archivos_modificados': 0,
                'ultima_sincronizacion': None
            }
        }
        
        for framework, config in self.estado_general.get('frameworks', {}).items():
            archivos = config.get('archivos_sincronizados', {})
            
            framework_status = {
                'total_archivos': len(archivos),
                'archivos_nuevos': len([a for a in archivos.values() if a.get('estado') == 'nuevo']),
                'archivos_modificados': len([a for a in archivos.values() if a.get('estado') == 'modificado']),
                'ultima_sincronizacion': config.get('ultima_sincronizacion')
            }
            
            status['frameworks'][framework] = framework_status
            
            # Actualizar resumen
            status['resumen']['total_archivos'] += framework_status['total_archivos']
            status['resumen']['archivos_nuevos'] += framework_status['archivos_nuevos']
            status['resumen']['archivos_modificados'] += framework_status['archivos_modificados']
        
        status['resumen']['total_frameworks'] = len(status['frameworks'])
        status['resumen']['ultima_sincronizacion'] = self.estado_general.get('estadisticas_globales', {}).get('ultima_sincronizacion')
        
        return status
    
    def generar_reporte(self, resultados: Dict[str, SincronizacionResult]) -> str:
        """Genera reporte de sincronización"""
        reporte = ["# 📊 REPORTE DE SINCRONIZACIÓN\\n"]
        reporte.append(f"**Fecha**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
        
        # Resumen global
        total_nuevos = sum(len(r.archivos_nuevos) for r in resultados.values())
        total_modificados = sum(len(r.archivos_modificados) for r in resultados.values())
        total_errores = sum(len(r.errores) for r in resultados.values())
        
        reporte.extend([
            "## 📈 Resumen Global\\n",
            f"- **Frameworks procesados**: {len(resultados)}",
            f"- **Archivos nuevos**: {total_nuevos}",
            f"- **Archivos modificados**: {total_modificados}", 
            f"- **Errores**: {total_errores}\\n"
        ])
        
        # Detalle por framework
        for framework, resultado in resultados.items():
            reporte.extend([
                f"## 📁 {framework}\\n",
                f"- **Tiempo ejecución**: {resultado.tiempo_ejecucion:.2f}s"
            ])
            
            if resultado.archivos_nuevos:
                reporte.append(f"- **Nuevos** ({len(resultado.archivos_nuevos)}):")
                for archivo in resultado.archivos_nuevos:
                    reporte.append(f"  - {archivo}")
            
            if resultado.archivos_modificados:
                reporte.append(f"- **Modificados** ({len(resultado.archivos_modificados)}):")
                for archivo in resultado.archivos_modificados:
                    reporte.append(f"  - {archivo}")
            
            if resultado.errores:
                reporte.append(f"- **Errores** ({len(resultado.errores)}):")
                for error in resultado.errores:
                    reporte.append(f"  - {error}")
            
            reporte.append("")
        
        return "\\n".join(reporte)

def main():
    parser = argparse.ArgumentParser(description='Sincronizador de Versiones PRP Framework')
    parser.add_argument('--update', action='store_true', help='Actualizar sincronización con repositorios')
    parser.add_argument('--status', action='store_true', help='Mostrar status actual')
    parser.add_argument('--framework', help='Sincronizar framework específico')
    parser.add_argument('--reporte', type=Path, help='Guardar reporte en archivo')
    
    args = parser.parse_args()
    
    try:
        sincronizador = SincronizadorVersiones()
        
        if args.status:
            status = sincronizador.obtener_status()
            print("\\n📊 STATUS DEL SISTEMA")
            print(f"Última sincronización: {status['resumen']['ultima_sincronizacion']}")
            print(f"Total frameworks: {status['resumen']['total_frameworks']}")
            print(f"Total archivos: {status['resumen']['total_archivos']}")
            print(f"Archivos nuevos: {status['resumen']['archivos_nuevos']}")
            print(f"Archivos modificados: {status['resumen']['archivos_modificados']}")
            
            for framework, info in status['frameworks'].items():
                print(f"\\n{framework}:")
                print(f"  Archivos: {info['total_archivos']}")
                print(f"  Nuevos: {info['archivos_nuevos']}")
                print(f"  Modificados: {info['archivos_modificados']}")
            
            return 0
        
        if args.update:
            if args.framework:
                logger.info(f"Sincronizando framework: {args.framework}")
                resultado = sincronizador.sincronizar_framework(args.framework)
                resultados = {args.framework: resultado}
            else:
                logger.info("Sincronizando todos los frameworks")
                resultados = sincronizador.sincronizar_todo()
            
            # Generar y mostrar reporte
            reporte = sincronizador.generar_reporte(resultados)
            print(reporte)
            
            if args.reporte:
                with open(args.reporte, 'w', encoding='utf-8') as f:
                    f.write(reporte)
                logger.info(f"Reporte guardado en: {args.reporte}")
            
            return 0
        
        parser.print_help()
        return 0
        
    except Exception as e:
        logger.error(f"Error durante sincronización: {e}")
        return 1

if __name__ == "__main__":
    exit(main())