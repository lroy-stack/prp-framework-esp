import { defineConfig } from 'vitest/config'

// Configuración de Vitest para el Servidor MCP
// Optimizada para testing de TypeScript en entorno Node.js con compatibilidad Cloudflare Workers
export default defineConfig({
  test: {
    // Entorno de testing Node.js (compatible con Cloudflare Workers)
    environment: 'node',
    
    // Habilita variables globales como describe, it, expect sin imports
    globals: true,
    
    // Archivo de configuración inicial para mocks y setup
    setupFiles: ['./tests/setup.ts'],
    
    // Configuraciones adicionales para servidor MCP
    testTimeout: 10000, // 10 segundos para operaciones de base de datos
    
    // Cobertura de código (opcional)
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json-summary', 'html'],
      exclude: [
        'node_modules/',
        'tests/',
        '**/*.config.js',
        '**/*.d.ts'
      ]
    }
  },
  
  // Configuración específica para desarrollo de servidor MCP
  define: {
    // Variables de entorno para testing
    __DEV__: true,
    __TEST__: true
  }
  
  /* 
   * NOTAS DE CONFIGURACIÓN:
   * - environment: 'node' es necesario para simular el runtime de Cloudflare Workers
   * - globals: true permite usar funciones de test sin imports explícitos
   * - setupFiles: './tests/setup.ts' configura mocks para OAuth, database, etc.
   * - testTimeout: Aumentado para permitir operaciones async de base de datos
   * - coverage: Configuración opcional para métricas de cobertura de código
   */
})