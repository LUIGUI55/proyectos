Claro, aquí tienes una introducción a NestJS en formato Markdown:

# Introducción a NestJS

## ¿Qué es NestJS?

NestJS es un framework progresivo para construir aplicaciones del lado del servidor con Node.js. Está construido con TypeScript y aprovecha las características modernas de JavaScript, así como los conceptos de programación orientada a objetos, programación funcional y programación reactiva.

## Características Principales

- **Modularidad**: NestJS permite organizar el código en módulos, lo que facilita la escalabilidad y el mantenimiento de la aplicación.
- **Inyección de Dependencias**: Proporciona un sistema de inyección de dependencias robusto y fácil de usar.
- **Soporte para TypeScript**: Aunque también se puede usar con JavaScript, NestJS está escrito en TypeScript, lo que proporciona tipado estático y otras características avanzadas del lenguaje.
- **Arquitectura basada en Decoradores**: Utiliza decoradores para definir controladores, servicios y otros componentes, lo que hace que el código sea más legible y estructurado.
- **Soporte para Middleware y Guardias**: Permite el uso de middleware y guardias para manejar la lógica de autorización y otras tareas transversales.
- **Integración con Bibliotecas y Frameworks Populares**: Se integra fácilmente con bibliotecas y frameworks como TypeORM, Mongoose, GraphQL, y más.

## Instalación

Para instalar NestJS, necesitas tener Node.js y npm (o yarn) instalados en tu sistema. Luego, puedes instalar el CLI de NestJS globalmente:

```sh
npm install -g @nestjs/cli
```

## Crear una Nueva Aplicación

Para crear una nueva aplicación NestJS, puedes usar el comando `nest new`:

```sh
nest new nombre-de-tu-aplicacion
```

Esto creará una nueva aplicación NestJS con una estructura de directorios básica.

## Estructura del Proyecto

Una aplicación NestJS típica tiene la siguiente estructura de directorios:

```
src/
 ├── app.controller.ts
 ├── app.controller.spec.ts
 ├── app.module.ts
 ├── app.service.ts
 └── main.ts
```

- **app.controller.ts**: Define los controladores que manejan las solicitudes HTTP.
- **app.module.ts**: Define el módulo raíz de la aplicación.
- **app.service.ts**: Define los servicios que contienen la lógica de negocio.
- **main.ts**: Es el punto de entrada de la aplicación.

## Ejemplo Básico

Aquí tienes un ejemplo básico de un controlador en NestJS:

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller('hello')
export class HelloController {
  @Get()
  getHello(): string {
    return 'Hola Mundo!';
  }
}
```

Y el módulo correspondiente:

```typescript
import { Module } from '@nestjs/common';
import { HelloController } from './hello.controller';

@Module({
  controllers: [HelloController],
})
export class AppModule {}
```

## Ejecutar la Aplicación

Para ejecutar la aplicación, usa el siguiente comando:

```sh
npm run start
```

Esto iniciará el servidor y podrás acceder a tu aplicación en `http://localhost:3000`.

## Conclusión

NestJS es un framework poderoso y flexible para construir aplicaciones del lado del servidor con Node.js. Su enfoque modular y su soporte para TypeScript lo hacen ideal para proyectos de cualquier tamaño. Con NestJS, puedes construir aplicaciones escalables y mantenibles de manera eficiente.

Para más información, puedes visitar la [documentación oficial de NestJS](https://docs.nestjs.com/).

