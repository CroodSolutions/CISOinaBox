# CISO in a Box favicon set (Bracket C)

Source of truth: `icon.svg`. Every other file here is rendered from it.

| File | Size | Use |
|---|---|---|
| icon.svg | vector | Primary favicon, modern browsers |
| favicon.ico | 16, 32, 48 | Legacy browsers, Windows |
| apple-touch-icon.png | 180x180 | iOS home screen (square, no transparency) |
| icon-192.png / icon-512.png | 192, 512 | Android and PWA |
| icon-mask.png | 512 | Android maskable (mark scaled into the safe zone) |
| manifest.webmanifest | | Web app manifest |

Put all files in the site root (or `public/` for Astro), then add to `<head>`:

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#050505">
```

Keep `sizes="32x32"` on the ICO link so Chrome picks the SVG.

Colors: tile #0b0b0b, brackets #ff0093, letter #f8f8f8 (matches the Telltale site palette).
