from flask import Blueprint, render_template, request, redirect, url_for
from models.Mood import Mood


mood_bp = Blueprint ('mood',__name__, url_prefix='/mood')

@mood_bp.route('/', methods=['GET', 'POST'])
def mood():
    #日にちを取得
    day=request.args.get('data')
    #過去のデータを取得
    if request.method == 'POST':
        mood = request.form.get('mood')

        if day:
         record =Mood.get_or_none(Mood.day==day)

         if record:
               record.mood=mood
               record.save()
         else:
               Mood.create(day=day,mood=mood)
        return redirect(url_for('day_data.day_data',data=day))



    if day:
         record =Mood.get_or_none(Mood.day==day)
         mood=record.mood if record else "データがありません"
    else:
         mood="日付が指定されていません"

    return render_template("mood_select.html",day=day,mood=mood)



