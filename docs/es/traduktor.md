---
title: traDUKtor Lite en español
slug: /es/traduktor
sidebar_position: 3
description: Manual operativo de traDUKtor Lite y gestión remota de equipos de acceso mediante DVRCP.
last_update:
  date: 2026-11-06
  author: DukeVilla
---

# Manual operativo de traDUKtor Lite

![Logo de traDUKtor](/img/traduktor-logo.png)

Español | [English](/docs/traduktor)

[Family brochure (English)](https://www.duke-villa.com/api/datasheets/datasheets%2Fen%2Ftraduktor%2FtraDUKtor_Family_Brochure.pdf) · [Ficha de familia (Español)](https://www.duke-villa.com/api/datasheets/datasheets%2Fes%2Ftraduktor%2FBrochure_Familia_traDUKtor.pdf)

**Versión estable de referencia:** `0.2.32`.

**Hardware de referencia:** Olimex ESP32-POE-ISO-16MB-IND.
**Alcance:** instalación, Translation, DVRCP, configuración, mantenimiento, respaldo, recuperación y diagnóstico.

:::info Manual vivo
Esta página es la referencia operativa vigente en español. Se actualiza en el mismo enlace. Las descargas históricas no representan el manual actual. Los nombres de menús y controles se conservan como aparecen en la interfaz.
:::

## Descripción del producto

traDUKtor Lite traduce protocolos en el sitio y ejecuta operaciones controladas sobre equipos compatibles para Fácil IoT. Las credenciales y las instrucciones específicas del equipo permanecen en el entorno local.

Solo una aplicación principal opera a la vez:

- **Translation** ejecuta hasta cinco líneas de conversión de protocolos.
- **DVRCP** reserva la ejecución para la orquestación desde Fácil IoT y la administración de equipos de acceso compatibles.

Cambiar de modo detiene los servicios de la aplicación anterior, pero conserva su configuración guardada.

## Primer acceso e inicio de sesión

Conecte traDUKtor a una red PoE y abra su dirección de administración. Después de un restablecimiento de fábrica, la recuperación directa usa `192.168.20.250/24`; configure el computador de administración en la misma subred.

Inicie sesión con una cuenta individual de administrador y cambie la credencial inicial durante la puesta en marcha. **Logout** cierra la sesión.

## Mapa de la interfaz

| Área | Vistas | Finalidad |
| --- | --- | --- |
| Dashboard | System Status, Lines, DVRCP, Mgmt & VPN | Evidencia operativa actual |
| Translation | Protocols, Lines | Modo de operación, perfiles y conversiones |
| DVRCP | Estado y modo de operación | Coordinación con Fácil IoT y equipos de acceso |
| Configuration | System, Network, Users, MQTT management | Configuración persistente |
| Maintenance | Firmware and files, Tools, Backup and files | Actualización, diagnóstico y recuperación |

Un valor no disponible o un servicio detenido no se interpreta como exitoso. Cada indicador confirma únicamente la comprobación que nombra.

## Dashboard

### System Status

**Operational** indica que la aplicación web y el núcleo responden. La actualización automática cada diez segundos consulta valores actuales sin cambiar ajustes.

**System** muestra hostname, serial, firmware, tiempo de funcionamiento, sincronización horaria y contador de eventos. **Ethernet** muestra controlador, enlace, modo de dirección, MAC, IP, subred y gateway. **Restart diagnostics** identifica la causa del último reinicio y el tiempo de funcionamiento actual.

### Lines

Resume los cinco espacios de traducción, extremos, configuración guardada, estado de ejecución y contadores. Una línea guardada no transporta datos hasta estar **Running**.

### DVRCP

Muestra el canal de administración autenticado hacia Fácil IoT, el modo exclusivo, la disponibilidad local de orquestación y el inventario persistente de **Terminal Units**. El estado IP y la administración autenticada son comprobaciones independientes.

### Mgmt & VPN

El enlace de administración y el transporte VPN opcional se verifican por separado. Compruebe destino, ruta, DNS, hora, certificados y autenticación. Alcanzar el broker no confirma una sesión MQTT autenticada.

## Translation

### Protocols

**Enable Translation** selecciona Translation y detiene DVRCP. Deshabilitar Translation detiene las líneas, pero conserva los perfiles.

| Protocolo | Ajustes principales del perfil |
| --- | --- |
| MQTT | Broker, puerto, TLS, identidad, usuario y contraseña, temas de publicación/suscripción y QoS |
| Telnet | Destino remoto, puerto TCP, rol de sesión y límites de conexión |
| SSH | Host, puerto, usuario, contraseña y rol cliente/servidor |
| Modbus TCP | Destino cliente o extremo servidor local, unidad y contexto de mapeo |
| HTTP REST | URL, método, contenido y tiempos de solicitud |

Los perfiles se reutilizan. Las contraseñas son de solo escritura; un campo vacío conserva el secreto guardado. Detenga todas las líneas dependientes antes de editar un perfil.

### Lines

1. Seleccione **Create line** en un espacio vacío.
2. Escriba **Line name**.
3. Seleccione **Input protocol** e **Input profile**.
4. Seleccione **Output protocol** y **Output profile**.
5. Guarde la línea mientras está detenida.
6. Iníciela y compruebe estado y contadores.

Use **Stop** antes de editar o eliminar. Eliminar una línea no elimina sus perfiles compartidos. Ante una falla, revise modo, estado de línea, Ethernet, gateway, DNS, ambos perfiles, servicios remotos, credenciales, hora para TLS y eventos.

## DVRCP

DVRCP permite configurar remotamente **equipos de acceso compatibles** desde Fácil IoT mediante traDUKtor. Fácil IoT define inventario, configuración deseada y acciones aprobadas. traDUKtor ejecuta las operaciones soportadas localmente mediante adaptadores validados y devuelve resultados observados.

![Arquitectura genérica de administración DVRCP](/img/dvrcp-access-es.svg)

La solución no está ligada a una marca de equipo. La compatibilidad se verifica por modelo, firmware y adaptador; disponer de una dirección IP no hace compatible automáticamente un equipo.

WiFi es opcional. Si el equipo administrado ofrece WiFi y la integración validada soporta acceso cautivo, su portal puede habilitarse y configurarse desde Fácil IoT. Las funciones de red y el control de acceso permanecen en el equipo. Una red enrutada puede funcionar sin portal cautivo.

### Arquitectura y modo de operación

Fácil IoT define el inventario asignado y la configuración deseada. traDUKtor ejecuta las utilidades del adaptador habilitado y reporta resultados mediante MQTT autenticado sobre TLS. El flujo enrutado contempla leer, comparar, aplicar, guardar y verificar las plantillas soportadas. Los roles Headend y Access se aplican únicamente si el perfil seleccionado implementa esa topología.

**Enable DVRCP** detiene Translation y sus líneas sin borrar la configuración guardada. Requiere **Managed by Fácil IoT** configurado y conectado. Deshabilitar un adaptador detiene sus operaciones específicas sin borrar el inventario. La aplicación de Fácil IoT conserva el nombre **MESH WiFi** en la interfaz; el servicio local de ejecución se denomina **DVRCP**.

### Coordinación y orden de puesta en marcha

Introduzca host/IP y puerto de Fácil IoT y autorice primero el serial de fábrica en la plataforma. La identidad MQTT es independiente de las credenciales de los equipos.

Para el perfil enrutado validado, habilite MESH WiFi en Fácil IoT, agregue el administrador registrado y configure primero el nodo 1 como Headend; después configure los nodos Access. Ese perfil admite hasta diez equipos compatibles por traDUKtor: un Headend y hasta nueve Access. No se supone que otros perfiles soporten la misma topología ni todas las operaciones.

Siga el [procedimiento de Fácil IoT](/docs/es/facil-iot#primera-configuracion-de-la-red-enrutada). Compare el estado observado con el deseado, aplique los cambios necesarios, espere su verificación y acepte con **Finish**. Guardar un plan de roles no configura por sí solo el equipo.

### Inventario persistente y comprobaciones autónomas

Abra **Dashboard > DVRCP > Terminal Units**. traDUKtor verifica el inventario al arrancar y normalmente cada **300 segundos (5 min)**. Actualiza IP, administración autenticada, identidad, direccionamiento e Internet de los equipos alcanzables. Ejecuta una prueba acotada de Internet desde cada equipo administrado usando su ruta normal; no exige una prueba separada desde cada interfaz.

Un equipo sin respuesta permanece en el inventario con su última identidad y dirección conocidas. La evidencia actual se informa por separado del historial. Solo una actualización explícita de Fácil IoT agrega, modifica o elimina registros; estar fuera de línea no solicita su eliminación.

| Columna | Significado |
| --- | --- |
| Name / Serial | Identidad asignada y reconciliada con el equipo detectado |
| Management IP | Dirección usada por traDUKtor para administrar el equipo |
| Route / Output | Ruta consultada: directa, específica o predeterminada, e interfaz de salida |
| Next hop | Próximo salto; para un destino directo, el propio destino |
| Manufacturer / Model / Firmware | Última identidad y software observados |
| IP | OK tras respuesta; Unreachable ante falla; Awaiting sin evidencia disponible |
| Mgmt | OK si la administración autenticada tuvo éxito; Awaiting si aún no se completó |
| Internet | OK si la prueba desde el equipo tuvo éxito; Unreachable ante falla; Awaiting si no se pudo ejecutar |

En el adaptador que usa Telnet, Mgmt refleja la sesión autenticada. Internet no certifica la navegación de cada subred ni la aplicación de un portal cautivo. Revise cualquier discrepancia de identidad antes de escribir configuración.

### Inventario y actualización temporal

La utilidad de inventario devuelve una instantánea consolidada de equipos, estado, caminos de administración y rutas. Fácil IoT la usa para **Routing** sin crear trabajos de diagnóstico por cada interfaz en cada actualización.

Al abrir Routing o seleccionar un administrador, se solicita una instantánea. Con **Refresh** desmarcado, la vista queda fija y el barrido autónomo de cinco minutos continúa. Al habilitar Refresh, puede solicitar temporalmente **10 s, 30 s, 1 min o 5 min**. Desmarcarlo, salir o cerrar el navegador libera la solicitud. Si el navegador desaparece inesperadamente, esta caduca y se retoma el intervalo normal. Nada de esto elimina inventario ni rutas.

### Rutas de retorno permanentes

En el perfil enrutado validado, traDUKtor instala redes de destino específicas a través de **Headend eth0**, conservando su gateway predeterminado independiente. El Headend enruta el tráfico Access y proporciona la salida mediante NAT en eth0.

Fácil IoT envía el plan confirmado después de configurar el Headend y lo actualiza al confirmar los Access. Las rutas se guardan y sobreviven a cortes de energía, reinicios y pérdida de Fácil IoT. Permanecen hasta que el controlador las modifique o retire explícitamente.

Una ruta activa solo en memoria no confirma persistencia. Compruebe el reconocimiento de guardado y corrija errores de almacenamiento antes de depender de la recuperación tras reinicio. Los cambios de IP o gateway en **Configuration > Network** se guardan por separado y requieren el reinicio indicado por la interfaz.

### Adaptadores y configuración segura

El adaptador validado expone las funciones soportadas por el equipo: pueden incluir identidad, salud, configuración, interfaces, rutas, switching, ACL, firewall, NAT, DHCP, WiFi y vecinos. No se supone que todos los adaptadores incluyan todas las utilidades.

Las escrituras usan operaciones permitidas y verificación sobre el destino. Detectar un equipo no autoriza modificarlo. **Finish** confirma la sesión terminada. **Cancel** ofrece restaurar elementos cuyo valor original se conoce e identifica los que conservarán su nuevo valor. Un valor original no observado no puede reconstruirse por suposición.

### Acceso cautivo opcional

Una red enrutada completa puede operar sin portal cautivo. **Captive Portal** está apagado por defecto. Habilite y configure la política desde Fácil IoT después de confirmar el soporte del equipo y adaptador y de estabilizar la red. Las restricciones experimentales previas no equivalen a un servicio cautivo puesto en marcha. IP, Mgmt e Internet no validan la autorización del cliente.

## Configuration

- **System:** hostname e identidad local. El serial de fábrica es de solo lectura. Reinicie cuando la interfaz lo requiera.
- **Network:** DHCP o IPv4 estática, dirección, prefijo, gateway y DNS. Use un solo gateway predeterminado y conserve el acceso de recuperación.
- **Users:** cuentas locales únicas. Las contraseñas nuevas contienen de 10 a 63 caracteres; la contraseña actual del administrador autoriza los cambios de acceso.
- **MQTT management:** habilitación, broker, puerto, confianza TLS y credencial emitida por Fácil IoT. Verifique la hora, guarde y confirme **Connected**. Nunca instale una clave privada del broker o de la CA en traDUKtor.

## Maintenance

### Firmware and files

**Last Release** consulta firmware firmado `stable`; **Last Beta**, el canal `lab`. **Install** verifica aplicación, hardware, canal, versión, longitud, SHA-256 y firma ECDSA antes de escribir el banco inactivo. **Rollback to previous firmware** cambia de banco y reinicia conservando ajustes, contraseñas y certificados. **Manual firmware upload** acepta un binario compatible firmado.

Mantenga energía y Ethernet durante la operación. Tras reiniciar, confirme que el banco activo esté **Validated**.

### Tools y respaldos

Ejecute diagnósticos acotados de ping, DNS, rutas, conectividad, hora y servicios. Sanee la información antes de compartirla.

- **Replication template:** exporta comportamiento reutilizable sin identidad, red de administración ni secretos. Importar deja detenidos los servicios.
- **Configuration backup:** conserva ajustes específicos sin exportar secretos. Revise la vista previa antes de restaurar.
- **System radiography:** exporta evidencia saneada de identidad, firmware, reinicio, red, servicios y eventos.

Revise todo lo importado antes de reiniciar o activar servicios.

### Reinicio y restablecimiento

**Restart** conserva los datos y aplica ajustes guardados. **Restore factory settings** borra configuración, cuentas y secretos y vuelve a `192.168.20.250/24`.

:::danger Restablecimiento de fábrica
Es destructivo. Confirme conectividad de recuperación y un respaldo aprobado antes de continuar.
:::

## Aceptación de una actualización estable

1. Registre versión, banco, IP y modo.
2. Consulte **Last Release** y verifique la versión ofrecida.
3. Instale en el banco inactivo.
4. Compruebe reinicio, Ethernet, hora, MQTT y modo seleccionado.
5. Verifique líneas o inventario retenidos.
6. Pruebe una traducción real o una operación soportada sobre un equipo administrado.
7. Confirme banco validado y disponibilidad de rollback.

## Contrato de seguridad de nivel 3

Una plantilla Headend o Access expresa un objetivo, no una condición supuesta. El trabajo seguro lee y conserva el estado actual, establece primero la administración, calcula un plan ordenado de operaciones permitidas, lo aplica, verifica interfaces, rutas y servicios, y se detiene o restaura si falla. El navegador no envía CLI arbitraria.

## Seguridad y soporte

Use firmware estable salvo pruebas controladas, usuarios y credenciales únicos, TLS y hora sincronizada. No exponga MQTT sin cifrar ni Telnet de los equipos a Internet. Respalde antes de cambiar red, modo, firmware o configuración de equipos. No interrumpa la energía durante una escritura, reinicio o restablecimiento.

Para soporte, entregue serial, firmware, banco activo, causa de reinicio, modo, hora aproximada de la falla y radiografía saneada. Nunca incluya contraseñas, tokens, claves privadas ni datos sin sanear.
