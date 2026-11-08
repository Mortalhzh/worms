#!/bin/bash
cd ~/worms-pub || exit 1
cp ~/index.html index.html
if ! grep -q 'manifest.json' index.html; then
  sed -i 's|<meta charset="utf-8">|<meta charset="utf-8">\n<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#1a1d2b">\n<link rel="icon" href="icon-192.png">\n<link rel="apple-touch-icon" href="icon-192.png">|' index.html
  sed -i 's|</body>|<script>if("serviceWorker" in navigator){navigator.serviceWorker.register("sw.js").catch(function(){});}</script>\n</body>|' index.html
fi
git add -A
git commit -m "update $(date +%F-%H%M)" || echo "nothing new"
git push
echo "deployed: https://mortalhzh.github.io/worms/"
