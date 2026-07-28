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

Then, in your project `settings.py`, add `tom_keck` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'tom_keck',
]
```

That's it. `tom_keck` implements the `observation_facilities()` AppConfig integration point,
so the Keck facility is discovered automatically — it does not need to be added to
`TOM_FACILITY_CLASSES` in your `settings.py`.

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
