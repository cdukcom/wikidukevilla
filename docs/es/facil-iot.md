---
title: Fácil IoT en español
slug: /es/facil-iot
sidebar_position: 4
description: Manual operativo de Fácil IoT, gestión remota DVRCP y portales cautivos WiFi opcionales.
last_update:
  date: 2026-11-06
  author: DukeVilla
---

# Manual operativo de Fácil IoT

![Logo de Fácil IoT](/img/facil-iot-logo.png)

Español | [English](/docs/facil-iot)

[Family brochure (English)](https://www.duke-villa.com/api/datasheets/datasheets%2Fen%2Ffacil-iot%2FFacil_IoT_Family_Brochure.pdf) · [Ficha de familia (Español)](https://www.duke-villa.com/api/datasheets/datasheets%2Fes%2Ffacil-iot%2FBrochure_Familia_Facil_IoT.pdf)

**Versión estable de referencia:** `0.1.19`.

**Appliance de referencia:** Protectli FW7225.
**Alcance:** operación, comunidades, equipos, alarmas, licencias, integraciones, DVRCP, MESH WiFi, configuración, mantenimiento y recuperación.

:::info Manual vivo
Esta página es la referencia operativa vigente en español. Se actualiza en el mismo enlace; las descargas históricas no representan el manual actual. Los nombres de menús y controles se conservan como aparecen en la interfaz.
:::

## Descripción del producto

Fácil IoT centraliza comunidades, Sites, gateways, sensores, alarmas, licencias, mapas, integraciones y administración de equipos de acceso compatibles. La operación local continúa durante una caída de Internet o del servicio central. Los estados mostrados deben proceder de evidencia actual o persistida; no se sustituyen datos no disponibles por ejemplos.

Fácil IoT proporciona interfaz web, API, base de datos, control MQTT y actualización firmada. Gateways y traDUKtors usan identidades MQTT únicas y temas con privilegios mínimos. traDUKtor ejecuta en el sitio las operaciones permitidas y conserva allí los secretos de los equipos. El navegador no recibe claves de firma, acceso a la base de datos ni ejecución arbitraria de comandos.

## Inicio de sesión y navegación

Use una cuenta individual. La sesión caduca tras treinta minutos sin actividad de puntero, teclado, pantalla táctil o desplazamiento. **Log out** cierra la sesión.

La navegación contiene **Dashboard**, **Communities**, **Devices**, **Alarms**, **Maps**, **Licenses**, **Users**, **Integrations**, **MESH WiFi**, **Maintenance** y **Settings**. Las búsquedas y filtros actúan sobre la página actual.

## Dashboard

Las tarjetas resumen equipos registrados, en línea, con telemetría y alarmas activas. **Operational status** muestra versión instalada, interfaz e IP de administración, tiempo de funcionamiento, arranque, causa de reinicio, hostname y hardware. El mapa usa únicamente coordenadas guardadas; alarmas y eventos representan sucesos reales. Los equipos recientes muestran telemetría real o su estado fuera de línea.

Revise Dashboard después de actualizar, reiniciar o cambiar la red.

## Communities

Las comunidades delimitan administración y licenciamiento. Use búsqueda y filtros de estado. Al crear o editar, registre organización, contacto y ubicación cuando corresponda, estado y notas.

Una comunidad contiene Sites, usuarios, equipos, gateways, licencias, servicios, integraciones, alarmas, traDUKtors y nodos. Desactivarla conserva el historial. Los Sites identifican la ubicación física o lógica de las instalaciones.

## Devices

Las pestañas separan clases de hardware. **Refresh** consulta el backend; **Online only** oculta activos sin evidencia actual.

### LoRaWAN

Registre identidad de hardware, modelo y perfil aprobados, comunidad, Site y coordenadas opcionales. La licencia y la conectividad de radio son independientes. El estado en línea requiere uplink o heartbeat.

### BLE

Registre el perfil aprobado y el identificador único. Una observación de gateway aporta telemetría, pero no cambia propietario ni Site.

### Gateways

Registre EUI, comunidad, Site, servicios LoRaWAN/BLE habilitados y enrolamiento MQTT único. Cada servicio informa su estado por separado. Editar metadatos no rota silenciosamente credenciales.

### traDUKtors

Registre nombre, serial de fábrica, comunidad, IP de administración, habilitación MQTT y permiso MESH WiFi. **Check IP** comprueba alcance desde la plataforma; **Management OK** requiere evidencia MQTT autenticada reciente. El trabajo de la aplicación requiere administración y permiso MESH.

### Terminal Units

Registre nombre, comunidad, Site, fabricante, serial, dirección de administración, credenciales y traDUKtor asignado. En el adaptador que usa Telnet, introduzca usuario y contraseña Telnet. Seleccione un adaptador validado para modelo y firmware: un fabricante o una IP no prueban compatibilidad ni autorizan escrituras.

La interfaz separa identidad **Configured** de fabricante, modelo, firmware y serial **Detected**. **Review** permite resolver discrepancias después de comprobar el equipo. Las credenciales son de solo escritura y se sincronizan de forma segura con el traDUKtor asignado.

## Alarms

La página resume condiciones abiertas, severidad, comunidad, estado y detección. **Acknowledge** registra conocimiento del operador; **Resolve** cierra con un evento de auditoría; **New route** crea automatización de notificación.

Una ruta contiene comunidad, nombre, integración, destinatario, sensor opcional, eventos separados por comas, severidades, plantilla y habilitación. Selecciones vacías de sensor, eventos o severidades permiten cualquier valor coincidente. Eliminar una ruta no elimina la integración ni el historial.

## Maps

Usa OpenStreetMap y coordenadas verificadas guardadas. La leyenda diferencia en línea, fuera de línea y descubrimiento pendiente. Sin cartografía, conserva coordenadas e informa que el fondo no está disponible.

## Licenses y servicios

Las licencias se asignan por comunidad y tecnología. Capacidad, uso y vigencia de LoRaWAN y BLE son independientes. Los servicios renovables registran estado y fechas. Una licencia válida autoriza uso; no confirma conectividad.

## Users

**New user** solicita:

- **User:** comienza con letra minúscula y usa minúsculas, números, punto, guion bajo o guion.
- **Role:** Administrator o Monitoring.
- **Display name** y **Email** opcional.
- **Password:** al menos doce caracteres.

Administrator configura y mantiene el appliance; Monitoring tiene acceso operativo restringido. **Delete** elimina acceso local tras confirmar.

## Integrations

Las integraciones de plataforma muestran servicios internos; las de comunidad conectan servicios externos aprobados. Según el proveedor, configure nombre, tipo, endpoint o cuenta, secreto de solo escritura, habilitación y comunidad.

Estar habilitada no sustituye una comprobación de salud ni una ruta o flujo. Las identidades MQTT siguen siendo individuales por equipo; una integración general no las reemplaza.

## DVRCP

Fácil IoT configura remotamente equipos de acceso compatibles mediante traDUKtor y DVRCP. Centraliza inventario y configuración deseada, muestra el estado observado para revisión, envía operaciones aprobadas y presenta resultados verificados. traDUKtor ejecuta las operaciones soportadas localmente mediante el adaptador validado; el equipo conserva sus funciones de red.

![Arquitectura genérica de administración DVRCP](/img/dvrcp-access-es.svg)

La solución es independiente de una marca específica. Las funciones disponibles dependen del modelo, firmware y adaptador. Si el equipo compatible dispone de WiFi y admite acceso cautivo, su portal puede habilitarse y configurarse desde Fácil IoT. WiFi y el portal cautivo son opcionales, no requisitos de la configuración remota básica.

## Primera configuración de la red enrutada {#primera-configuracion-de-la-red-enrutada}

La interfaz conserva el nombre **MESH WiFi** para esta aplicación. El siguiente procedimiento Headend/Access corresponde al perfil enrutado que implementa esos roles. La red puede operar permanentemente sin portal cautivo; **Captive Portal** está apagado por defecto y su puesta en marcha es una etapa aparte.

### Preparación

Prepare comunidad y Site, un traDUKtor registrado con MQTT autenticado operativo y equipos compatibles con adaptador validado, direcciones de administración y credenciales conocidas. Compruebe que traDUKtor alcance inicialmente el Headend en su red de administración: una ruta Access remota no se establece antes de existir ese camino.

El perfil validado usa hasta diez equipos compatibles: un Headend y hasta nueve Access por traDUKtor. No traslade la topología a otros perfiles sin validación.

### 1. Global

Abra **MESH WiFi > Global** y habilite la aplicación. Global no reemplaza el enrolamiento MQTT individual ni habilita automáticamente restricciones cautivas.

### 2. MESH traDUKtors

Seleccione los administradores registrados del contexto correspondiente y habilite su participación. Compruebe MQTT y permiso de la aplicación. En traDUKtor deben estar habilitados DVRCP y el adaptador validado para ejecutar las operaciones soportadas.

### 3. MESH Terminal Units

Seleccione traDUKtor y use **Open Terminal Units in Devices** para registrar primero el Headend. Registre dirección, identidad y credenciales y asigne el equipo al administrador.

Asigne **Headend** al primer nodo y guarde el plan de roles. Los Access siguen en las posiciones 2 a 10. Las flechas ordenan los Access y ese orden participa en la configuración generada. Guardar roles no demuestra que se hayan aplicado ajustes.

### 4. Configuration

El diálogo compara el estado **observed** con el **target** del rol y Site. Revise direccionamiento, rutas, servicios y nombres.

| Estado | Significado y acción |
| --- | --- |
| Matches template | El valor observado coincide; no requiere cambio |
| Change required | El valor difiere; revise el objetivo antes de aplicar |
| Observation required | No se observó el original; no suponga coincidencia ni posibilidad de restaurarlo |

1. Revise la comparación. Use **Edit recommendation** solo para un ajuste deliberado. **Advanced actions** permite cambios expertos soportados, aunque la lista normal coincida.
2. Seleccione **Apply configuration** y confirme los cambios revisados. Si todo coincide, Apply queda deshabilitado.
3. Observe envío, contacto, carga, guardado, confirmación y verificación operativa. Guardar un objetivo no demuestra éxito.
4. Tras aplicar y verificar, seleccione **Finish** para aceptar y cerrar. Finish termina la oportunidad de rollback de la sesión.
5. Si elige **Cancel** después de aplicar, lea qué elementos pueden restaurarse y cuáles conservarán ajustes nuevos por desconocerse el original. Confirmar restaura lo indicado; rechazar la confirmación mantiene la sesión abierta.

Ante una falla, revise y restaure o corrija antes de continuar. Conserve el Headend alcanzable.

### 5. Unidades Access

Con el Headend configurado y confirmado:

1. Registre Access en **Devices > Terminal Units** y asígnelo al mismo traDUKtor.
2. Seleccione el administrador en **MESH Terminal Units**, asigne **Access** y guarde el plan.
3. Abra **Configuration**, revise, aplique, espere verificación y confirme con **Finish**.
4. Repita hasta nueve Access, comprobando orden y direcciones antes de cada plantilla.

Los Access confirmados agregan sus redes al plan. Responder a ping no sustituye verificar configuración.

### 6. Routing

Abra **Routing** y seleccione traDUKtor. La primera instantánea se carga automáticamente; no hay botón Verify independiente. El dibujo muestra administrador, Headend, Access, nombres, IP y tres estados.

| Estado | OK significa | Si falla |
| --- | --- | --- |
| IP | traDUKtor alcanzó la dirección de administración | Revise energía, direcciones, camino Headend y ruta |
| Mgmt | La sesión de administración tuvo éxito | Revise IP, servicio, credenciales e identidad |
| Internet | Una prueba desde el equipo por su ruta normal alcanzó Internet | Revise ruta, salida Headend, NAT y restricciones; ICMP no identifica por sí solo la causa |

Internet no valida cada interfaz, la autenticación de clientes ni el portal cautivo. No interprete evidencia pendiente como éxito. Los equipos fuera de línea conservan inventario e identidad conocida.

**Static routes** muestra destino, próximo salto y estado. **Saved** confirma almacenamiento permanente; **Active** sin guardado no prueba persistencia; **Pending** requiere revisión. Las rutas específicas llegan por Headend eth0 sin reemplazar el gateway predeterminado de traDUKtor.

Si Headend está incompleto, vuelva a Configuration. Al tener todos los equipos puestos en marcha con IP, Mgmt e Internet OK y las rutas guardadas, termina la etapa enrutada. Puede operar sin portal cautivo.

### Actualización de Routing

| Control o evento | Comportamiento |
| --- | --- |
| Abrir Routing o seleccionar administrador | Solicita una instantánea |
| Refresh desmarcado | Conserva la instantánea aunque pasen más de cinco minutos |
| Selector | Predeterminado 5 min; alternativas 10 s, 30 s y 1 min; elegir no inicia consultas |
| Refresh marcado | Solicita inventario y diagnóstico temporal con ese intervalo |
| Cambiar intervalo habilitado | Actualiza sin superponer consultas |
| Desmarcar Refresh | Detiene solicitudes, libera el intervalo y conserva lo mostrado |
| Salir, cambiar administrador o cerrar navegador | Termina la sesión temporal; no elimina inventario, ajustes ni rutas |

traDUKtor barre inventario al arrancar y cada cinco minutos independientemente del navegador. La solicitud temporal caduca si el navegador desaparece sin liberarla. Volver desde segundo plano no reinicia consultas silenciosamente: habilite Refresh o entre de nuevo para otra instantánea.

Use intervalos cortos durante diagnóstico y desactívelos al terminar. Eliminar equipos o retirar rutas exige una actualización explícita. Cerrar la pantalla, perder el controlador o tener equipos fuera de línea no borra rutas guardadas.

### Portal cautivo opcional

Si equipo y adaptador soportan WiFi y acceso cautivo, habilite y configure el portal desde Fácil IoT tras estabilizar la red. Mantenga **Captive Portal** apagado para una red sin restricciones. Reglas de pruebas previas pueden continuar restringiendo tráfico; Internet OK en el equipo no valida la navegación completa de un cliente cautivo.

## Settings

### General

Configure nombre de aplicación, idioma disponible, zona horaria, formato de fecha, NTP principal y secundario. La hora correcta es necesaria para eventos, certificados y verificación de versiones. Esta traducción del manual no cambia el idioma del software.

### Notifications

Hay notificaciones internas, email y WhatsApp cuando sus integraciones están activas. Los eventos incluyen alarmas críticas y prioritarias, equipos fuera de línea y batería baja.

### Red del appliance

Solo la interfaz principal instala gateway predeterminado. Configure hostname, DHCP o IPv4 estática, dirección, prefijo, gateway, DNS principal/secundario, VLAN 802.1Q opcional e ID, e IPv6. La LAN de recuperación no debe agregar otra ruta predeterminada.

Aplicar cambios requiere confirmación, respaldo automático y rollback si falla la validación. Mantenga recuperación directa.

## Maintenance

Presenta estado, actualizaciones firmadas, diagnósticos, logs, respaldos, recuperación y versión anterior.

- **Last Release:** canal firmado `stable`.
- **Last Beta:** canal firmado `lab`.
- La carga desde el navegador acepta paquetes `.fiot` firmados.
- La activación valida el paquete, respalda PostgreSQL, verifica Compose, cambia versión atómicamente, inicia servicios y comprueba salud.
- El rollback de código y la restauración de base de datos son operaciones diferentes.

Conserve energía y red. Después del regreso al inicio de sesión, verifique versión, tiempo de funcionamiento, base de datos, equipos, MQTT y versión anterior.

## Límite de confianza MQTT

El broker protegido usa identidades y ACL separadas. Los gateways se enrolan por EUI; los traDUKtors, por serial y credencial única. Administración general y permiso MESH son independientes. Serial o EUI nunca son contraseñas. MQTT público requiere TLS y autenticación; no se expone 1883 sin cifrar a Internet.

## Respaldo y recuperación

Respalde PostgreSQL antes de activar una versión. Volver al código anterior no restaura automáticamente base de datos, certificados, secretos ni red. Mantenga procedimientos probados para recuperar administrador, código, base de datos, LAN y appliance completo.

No elimine volúmenes persistentes ni depure contenedores de todo el host sin identificar propietario y confirmar respaldo recuperable.

## Aceptación de una actualización estable

1. Registre versión y hardware.
2. Consulte **Last Release** y confirme canal, tamaño, firma y versión.
3. Instale y observe progreso.
4. Confirme salud y regreso al inicio de sesión.
5. Verifique versión, tiempo de funcionamiento, base de datos, usuarios, equipos, MQTT y versión anterior.
6. Repita administración, configuración confirmada, rutas guardadas e IP/Mgmt/Internet de cada equipo.

## Seguridad y soporte

Use cuentas individuales, privilegios mínimos, credenciales MQTT únicas y ACL por equipo. Sincronice hora y respalde antes de cambiar red, versión, rutas o políticas cautivas. Cada indicador valida solo su comprobación; no declare aplicado un cambio sin verificar el destino.

Para soporte, entregue versión, hardware, hostname, tiempo de funcionamiento, causa de arranque, hora de falla, comunidad/Site y logs saneados. Para DVRCP, agregue serial/versión de traDUKtor, identidad y firmware del equipo, rol, posición y etapa fallida. Nunca incluya contraseñas, tokens, claves privadas ni datos de clientes sin sanear.
