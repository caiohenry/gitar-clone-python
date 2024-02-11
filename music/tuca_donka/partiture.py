from game.notes import Note

class PartitureTucaDonka:
    
    def __init__(self):
        
        self.notes: list[Note] = []
        self.currenty_time: int = 0
        
        
    def first_feat(self, sum: int = None, last_feat: bool = False, second: bool = False):
        
        if sum is not None:
            
            self.currenty_time += sum
        
        for _ in range(3):
            
            self.currenty_time += 350
            
            note = Note(time = self.currenty_time, columns = [0])
            
            self.notes.append(note)
            
        if not last_feat:
            
            self.currenty_time += 400
            
            self.notes.append(Note(time = self.currenty_time, columns = [1]))
            
            self.currenty_time += 150
            
            self.notes.append(Note(time = self.currenty_time, columns = [2 if second else 3]))
    
    def second_feat(self, sum: int = None):
        
        if sum is not None:
            
            self.currenty_time += sum
            
        
        for note_column in range(3):
            
            if note_column == 2:
        
                self.currenty_time -= 50
            
            self.currenty_time += 400
                
            self.notes.append(Note(time = self.currenty_time, columns = [note_column]))

            
    def drop(self, sum = None):
        
        if sum is not None:
            self.currenty_time += sum
        
        self.notes.append(Note(time = self.currenty_time, columns = [2, 3]))
        self.currenty_time += 350
        self.notes.append(Note(time = self.currenty_time, columns = [0]))
        self.currenty_time += 150
        self.notes.append(Note(time = self.currenty_time, columns = [1]))
        
        for _ in range(2):
            self.currenty_time += 400
            self.notes.append(Note(time = self.currenty_time, columns = [1,2]))
            
    
    def berofe_drop(self, sum=None):
        
        if sum is not None:
            self.currenty_time += sum
            
        self.notes.append(Note(time = self.currenty_time, columns = [1, 2], type=False))
    
    def get_partiture(self):
        
        partiture = PartitureTucaDonka()
        # partiture.berofe_drop(sum=200)
        partiture.first_feat()
        partiture.first_feat(100, second=True)
        partiture.first_feat(100)
        partiture.first_feat(100, last_feat=True)
        partiture.second_feat(1300)
        partiture.second_feat(700)
        partiture.second_feat(500)
        partiture.second_feat(700)
        partiture.second_feat(500)
        partiture.second_feat(700)
        partiture.second_feat(500)
        partiture.second_feat(700)
        partiture.drop(500)
        partiture.drop(500)
        partiture.drop(500)
        partiture.berofe_drop(600)
        partiture.drop(2300)
        partiture.drop(500)
        partiture.drop(500)
        partiture.first_feat(1800)
        partiture.first_feat(100, second=True)
        partiture.first_feat(100)
        partiture.first_feat(100, last_feat=True)
        return partiture.notes
    
    def __str__(self) -> str:
        return f"{self.notes}"          
