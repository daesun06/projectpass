Dont know how to setup reflex on my desktop. Did the things that the instructions said. No use. Just starting the same demo app they have.
So i can't start my programm on this desktop meaning i dont know how it looks and works.

# New task
1. Add a sliding sidebar where there is two buttons. One is to go the home page, the other is to go to the paswwords table page.
2. Add the table page center and align it, make it look cool.
3. Storage only the browser and user name. Make a button request your password where you input your master password and it returns you the same password in a pop-up message.
4. Add a copy to clipboard or at least do a decorative button to copy it.



```python
import json

class ComplexLocalStorageState(rx.State):
    data_raw: str = rx.LocalStorage("{}", sync=True)
    data: dict[str, list[str]] = {}
    
    def _save_settings(self):
        self.data_raw = json.dump(self.data)

    def load_settings(self):
        self.data = json.load(self.data_raw)

    def add_record(self, name: str, website: str):
        if self.data[name]:
            self.data[name].append(website)
        else:
            self.data[name] = [website]
            
    def delete_record(self, name: str, website: str):
        if not self.data[name]:
            return 

        self.data[name] = [site for site in self.data[name] if site != website]
        self._save_settings()
```

# Added
1. New page with the passwords table
2. Routes
3. Updated the navbar
