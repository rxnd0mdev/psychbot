import json
def cooktherhythms(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            rawtext = f.read()
            data = json.loads(rawtext)
        hasdangerousstuff = "Halo Note" in rawtext or '"sectionNotes"' in rawtext # only triggers if there is halo notes in json
        songdata = data.get('song', data)
        sections = songdata.get('notes', [])
        noterecipe = []
        
        print(f"[*] scan mode: {'PARANOID (filter on)' if hasdangerousstuff else 'RELAXED (No traps)'}")

        for block in sections:
            if not isinstance(block, dict): continue
            musthit = block.get('mustHitSection', False)
            notesinsection = block.get('sectionNotes', [])    
            for n in notesinsection:
                if len(n) < 2: continue
                if hasdangerousstuff and len(n) > 3:
                    notetype = n[3]
                    if notetype not in [0, "", None, False, "0"]:
                        continue   
                atms = n[0]
                whicharrow = n[1]
                howlong = n[2] if len(n) > 2 else 0
                if (musthit and 0 <= whicharrow <= 3) or (not musthit and 4 <= whicharrow <= 7):
                    targetkey = whicharrow if whicharrow <= 3 else whicharrow - 4
                    islong = howlong > 20
                    
                    noterecipe.append({
                        'ms': atms, 
                        'finger': targetkey, 
                        'end': atms + howlong if islong else 0,
                        'isstretch': islong
                    })
        
        noterecipe.sort(key=lambda x: x['ms'])
        return noterecipe
    except Exception as e:
        print(f"[!] Error reading JSON: {e}")
        return None
