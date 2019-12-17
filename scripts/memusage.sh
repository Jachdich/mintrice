ps axk-rss -o comm,%mem,rss | head -n30 | python3 ~/.scripts/memanalysis.py
