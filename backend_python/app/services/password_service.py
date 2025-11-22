from app.models.password_models import PasswordAnalyzeResponse

class PasswordService:

    def analyze_password(self,password:str) -> PasswordAnalyzeResponse:
        score=0
        issues=[]
        suggestions = []

        #Length-Based scoring
        if len(password)<6:
            score+=10
            issues.append("password is too short")
            suggestions.append("use atleast 8-12 characters")
        elif len(password)<10:
            score+=30
            suggestions.append("Longer passwords are more secure(12+ Chars)")
        else:
            score+=40

        #Character checks
        if any(c.islower() for c in password):
            score+=10
        else:
            issues.append("No lowercase letters")
            suggestions.append("Add some lowercase letters")

        if any(c.isupper() for c in password):
            score+=10
        else:
            issues.append("No uppercase letters")
            suggestions.append("Add some uppercase letters")
        if any(c.isdigit() for c in password):
            score+=10
        else:
            issues.append("No digits")
            suggestions.append("Add at least one digit")
        
        #Cap score at 100
        score = min(score,100)

        #Strength label
        if score<40:
            strength = "Weak"
        elif score<70:
            strength = "Medium"
        else:
            strength = "Strong"
        
        return PasswordAnalyzeResponse(
            score = score,
            strength = strength,
            issues = issues,
            suggestions = list(dict.fromkeys(suggestions))
        )

password_service = PasswordService()