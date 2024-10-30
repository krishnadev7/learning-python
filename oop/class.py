class Person:
      def __init__(self,name):
          self.name = name
      def talk(self):
            print(f"Hi I'm {self.name}") 


krish = Person("krishnadev")
krish.talk()