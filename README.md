# Theme & Wallpaper Switcher

Un script en Python que cambia automáticamente entre tema claro y oscuro de Windows según la hora del día.

## 🌟 Características

- **Cambio automático**: Alterna entre tema claro y oscuro según la hora configurada
- **Inicio automático**: Puede configurarse para iniciar con Windows
- **Registro detallado**: Mantiene un log de todas las acciones

## 📋 Requisitos

- Windows 10/11
- Python 3.6+
- Módulo pywin32 (`pip install pywin32`)

## 🚀 Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/jerkey06/Theme-swicher.git
   cd Theme-swicher
   ```

2. **Instala las dependencias**:
   ```bash
   pip install pywin32
   ```

3. **Configura el script** (ver sección de configuración)

4. **Ejecuta el script**:
   ```bash
   python src/theme_switcher.py
   ```

5. **Para que inicie automáticamente con Windows**:
   ```bash
   python src/theme_switcher.py --install
   ```

## ⚙️ Configuración

### Configuración de horarios

Edita estos valores en la sección `Config` del script:

```python
# Horarios para cambiar el tema (formato 24 horas)
LIGHT_THEME_START = 7  # 7:00 AM - Cambia a tema claro
DARK_THEME_START = 19  # 7:00 PM - Cambia a tema oscuro
```

## 🛠️ Cómo funciona

El script realiza las siguientes acciones:

1. Comprueba la hora actual.
2. Determina si debe usar tema claro u oscuro según la configuración.
3. Si es necesario cambiar el tema:
   - Cambia la configuración del registro de Windows para alternar entre tema claro y oscuro.
4. Repite la comprobación cada minuto.

## 📋 Registro de actividad

El script crea un archivo `theme_switcher.log` que registra todas las acciones y posibles errores. Este archivo puede ser útil para diagnosticar problemas si el script no funciona como se espera.

## 📱 Solución de problemas

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

Emi - contactojkemi@gmail.com

Link del proyecto: [https://github.com/jerkey06/Theme-swicher](https://github.com/jerkey06/Theme-swicher)