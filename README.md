# Theme & Wallpaper Switcher

Un script en Python que cambia automáticamente entre tema claro y oscuro de Windows según la hora del día, y además configura fondos de pantalla diferentes usando Wallpaper Engine.

## 🌟 Características

- **Cambio automático**: Alterna entre tema claro y oscuro según la hora configurada
- **Integración con Wallpaper Engine**: Cambia los fondos de pantalla automáticamente
- **Inicio automático**: Puede configurarse para iniciar con Windows
- **Registro detallado**: Mantiene un log de todas las acciones

## 📋 Requisitos

- Windows 10/11
- Python 3.6+
- Módulo pywin32 (`pip install pywin32`)
- [Wallpaper Engine](https://store.steampowered.com/app/431960/Wallpaper_Engine/) instalado

## 🚀 Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/theme-wallpaper-switcher.git
   cd theme-wallpaper-switcher
   ```

2. **Instala las dependencias**:
   ```bash
   pip install pywin32
   ```

3. **Configura el script** (ver sección de configuración)

4. **Ejecuta el script**:
   ```bash
   python theme_wallpaper_switcher.py
   ```

5. **Para que inicie automáticamente con Windows**:
   ```bash
   python theme_wallpaper_switcher.py --install
   ```

## ⚙️ Configuración

### Configuración de horarios

Edita estos valores en la sección `Config` del script:

```python
# Horarios para cambiar el tema (formato 24 horas)
LIGHT_THEME_START = 7  # 7:00 AM - Cambia a tema claro
DARK_THEME_START = 19  # 7:00 PM - Cambia a tema oscuro
```

### Configuración de Wallpaper Engine

#### Paso 1: Encontrar los ID de tus fondos favoritos

1. **Abre Wallpaper Engine** desde Steam o desde tu escritorio.

2. **Busca el fondo que quieres usar para el día** (tema claro) en tu biblioteca o en el Workshop.

3. **Obtén el ID del Workshop** de este fondo:
   - Si ya está en tu biblioteca, haz clic derecho en él y selecciona "Copiar URL"
   - El ID es un número largo (ej. 1234567890) que aparece después de "id=" en la URL
   - Ejemplo de URL: `https://steamcommunity.com/sharedfiles/filedetails/?id=1234567890`

4. **Repite el proceso para el fondo de noche** (tema oscuro).

#### Paso 2: Actualiza el script con los IDs

Modifica estos valores en la sección `Config` del script:

```python
# IDs de los fondos de pantalla para Wallpaper Engine
LIGHT_WALLPAPER_ID = "1234567890"  # Reemplaza con tu ID para el fondo de día
DARK_WALLPAPER_ID = "0987654321"   # Reemplaza con tu ID para el fondo de noche
```

#### Paso 3: Verifica la ruta de instalación

Comprueba que la ruta a Wallpaper Engine sea correcta para tu sistema:

```python
# Ruta de instalación de Wallpaper Engine (ajustar según tu instalación)
WALLPAPER_ENGINE_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\wallpaper_engine\\wallpaper32.exe"
```

## 🛠️ Cómo funciona

El script realiza las siguientes acciones:

1. Comprueba la hora actual.
2. Determina si debe usar tema claro u oscuro según la configuración.
3. Si es necesario cambiar el tema:
   - Cambia la configuración del registro de Windows para alternar entre tema claro y oscuro.
   - Comunica con Wallpaper Engine para cambiar el fondo de pantalla.
4. Repite la comprobación cada minuto.

## 📋 Registro de actividad

El script crea un archivo `theme_switcher.log` que registra todas las acciones y posibles errores. Este archivo puede ser útil para diagnosticar problemas si el script no funciona como se espera.

## 📱 Solución de problemas

### Wallpaper Engine no cambia el fondo

El script intenta dos métodos diferentes para cambiar el fondo:

1. **Método 1**: Usa la integración directa con Steam.
2. **Método 2**: Modifica el archivo de configuración de Wallpaper Engine.

Si ninguno de estos métodos funciona:

- Verifica que los IDs de Workshop sean correctos.
- Comprueba la ruta de instalación de Wallpaper Engine.
- Asegúrate de que Wallpaper Engine esté configurado para iniciar con Windows.
- Consulta el archivo `theme_switcher.log` para más detalles sobre el error.

### El tema de Windows no cambia

- Asegúrate de ejecutar el script como administrador para poder modificar el registro de Windows.
- Si usas una versión antigua de Windows, es posible que no soporte el cambio de tema mediante el registro.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar este script:

1. Crea un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add some amazing feature'`)
4. Haz push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

[Tu Nombre] - [tu@email.com]

Link del proyecto: [https://github.com/tu-usuario/theme-wallpaper-switcher](https://github.com/tu-usuario/theme-wallpaper-switcher)