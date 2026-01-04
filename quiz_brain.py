class QuizBrain:
    
    def __init__(self,qlist): #defining attributes
        self.qno=0
        self.qlist=qlist
        self.score=0

    def question_left(self): #checking for if questions left
        return self.qno<len(self.qlist)

    def nextquestion(self): #displaying questions
        currentq=self.qlist[self.qno]
        self.qno+=1
        user_answer=input(f"Q.{self.qno}:{currentq.text}(True/False): ")
        correct_answer=currentq.answer
        self.checkanswer(user_answer,correct_answer)

    def checkanswer(self,user_answer, correct_answer): #validating answers
        if user_answer.lower()==correct_answer.lower():
            print("That was correct")
            self.score+=1
            print(f"You answered {self.score} questions right out of {self.qno}")
        else:
            print("That was wrong")
            print(f"The correct answer is :{correct_answer}")
            print(f"You got {self.score}  question(s) right out of {self.qno}")