# Definir Contrato API Entre Backend y Frontend

Funcionalidad: $ARGUMENTS

## Tarea: Crear especificación detallada de contrato API para coordinación backend/frontend

1. **Definir endpoints RESTful**:

   ```yaml
   Base URL: /api/v1/{feature}

   Endpoints:
   - GET /api/v1/{features}
     Query params: page, size, sort, filter
     Response: Page<{Feature}Response>

   - GET /api/v1/{features}/{id}
     Path param: id (Long)
     Response: {Feature}Response

   - POST /api/v1/{features}
     Body: {Feature}Request
     Response: {Feature}Response (201 Created)

   - PUT /api/v1/{features}/{id}
     Path param: id (Long)
     Body: {Feature}Request
     Response: {Feature}Response

   - DELETE /api/v1/{features}/{id}
     Path param: id (Long)
     Response: 204 No Content
   ```

2. **Definir DTOs de request/response**:

   ```typescript
   // Request DTO (para POST/PUT)
   interface {Feature}Request {
     name: string;        // min: 2, max: 100
     description?: string; // max: 1000
     // Agregar campos específicos del dominio
   }

   // Response DTO (para GET)
   interface {Feature}Response {
     id: number;
     name: string;
     description?: string;
     createdAt: string;   // ISO 8601
     updatedAt: string;   // ISO 8601
     // Agregar campos computados
   }

   // Wrapper de respuesta paginada
   interface Page<T> {
     content: T[];
     totalElements: number;
     totalPages: number;
     size: number;
     number: number;
   }
   ```

3. **Definir respuestas de error**:

   ```json
   {
     "timestamp": "2024-01-20T10:30:00Z",
     "status": 400,
     "error": "Bad Request",
     "message": "Validation failed",
     "path": "/api/v1/{features}",
     "errors": [
       {
         "field": "name",
         "message": "Name is required"
       }
     ]
   }
   ```

4. **Definir reglas de validación**:
   - Backend: Anotaciones Bean Validation
   - Frontend: Esquemas Zod correspondientes

   ```
   name: requerido, 2-100 caracteres
   description: opcional, máx 1000 caracteres
   email: formato de email válido
   date: formato ISO 8601
   ```

5. **Definir códigos de estado**:
   - 200: OK (GET, PUT)
   - 201: Created (POST)
   - 204: No Content (DELETE)
   - 400: Bad Request (validación)
   - 404: Not Found
   - 409: Conflict (duplicado)
   - 500: Internal Server Error

6. **Requerimientos de integración**:
   - CORS: Permitir origen del frontend
   - Content-Type: application/json
   - Autenticación: Bearer token (si es necesario)
   - Paginación: formato Spring Pageable
   - Ordenamiento: field,direction (ej., "name,asc")

7. **Notas de implementación backend**:

   ```java
   // Campos de Entity coinciden con response DTO
   // Usar MapStruct para mapeo de DTO
   // Convenciones de nomenclatura de métodos Repository
   // Validación en capa Service
   ```

8. **Notas de implementación frontend**:
   ```typescript
   // Esquemas Zod coinciden con reglas de validación
   // Cliente API con configuración base
   // Hooks TanStack Query
   // Utilidades de manejo de errores
   ```

Guardar este contrato como: `PRPs/contracts/{feature}-api-contract.md`

Compartir este archivo entre equipos de backend y frontend para alineación.