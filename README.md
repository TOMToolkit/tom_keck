# tom_keck
WM Keck Observatory facility module for TOM Toolkit.

🚧 pre-release work-in-progress 🚧

# Prerequisites
TODO: _List prerequistes here (like credentials, ToO observing program, etc) and links to fulfull them_.

# Installation

Install the module into your TOM environment:

```shell
pip install tom-keck
```

1. In your project `settings.py`, add `tom_keck` to your `INSTALLED_APPS` setting:

    ```python
    INSTALLED_APPS = [
        ...
        'tom_keck',
    ]
    ```

2. Add `tom_keck.keck.KeckFacility` to the `TOM_FACILITY_CLASSES` in your TOM's
`settings.py`:
   ```python
    TOM_FACILITY_CLASSES = [
        'tom_observations.facilities.lco.LCOFacility',
        ...
        'tom_keck.keck.KeckFacility',
    ]
   ```   

## Configuration

For TOM-wide credentials, include the following settings inside the `FACILITIES` dictionary inside `settings.py`:

```python
    FACILITIES = {
        ...
        'KECK': {
            'KECK_USERNAME': os.getenv('KECK_USERNAME', 'set me'),
            'KECK_PASSWORD': os.getenv('KECK_PASSWORD', 'set me'),
        },
    }
```

**User-specific** credentials can be added by individual users via their User Profile page. When both user-specific credentials and TOM-wide credentials are present, user-specific credential take precedence.
