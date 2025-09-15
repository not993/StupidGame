class Item():
    def __init__(self, item_name, item_desc):
        self.name = item_name
        self.description = item_desc
        self.visible = None
        self.drop = None

    def set_name(self, name_to_set):
        self.name = name_to_set

    def set_description(self, description_to_set):
        self.description = description_to_set

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def hide(self):
        self.visible = False
    
    def show(self):
        self.visible = True

    def drop(self):
        self.drop = True

    def static(self):
        self.drop = False
    
    def describe(self):
        print(f"""{self.name}
{"."*len(self.name)}
{self.description if self.description else ''}
""")

if __name__ == "__main__":
    sword = Item('Black Shard', 'a shard of a dark, opaque, glassy material.')

    sword.describe()