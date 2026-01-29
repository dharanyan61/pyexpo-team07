def place_call(self):
        self.stop_siren()
        contact = FAMILY_CONTACTS[self.call_index]

        self.status.text = f"Calling {contact['name']}..."
        webbrowser.open(f"tel:{contact['number']}")

        
        self.call_index = (self.call_index + 1) % len(FAMILY_CONTACTS)

   

def start_siren(self):
     if self.siren and not self.siren_on:
        self.siren.loop = True
        self.siren.play()
        self.siren_on = True

def stop_siren(self):
     if self.siren and self.siren_on:
         self.siren.stop()
         self.siren_on = False