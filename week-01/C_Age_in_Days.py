num=int(input())
years,months,days=0,0,0

if num>=365:
    years=num//365
    num=num-(years*365)
if num>=30:
    months=num//30
    num=num-(months*30)
if num>=0:
    days=num

print(f"{years} years\n{months} months\n{days} days")
