from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Question, Choice, Submission


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        submission = Submission.objects.create(user=request.user, course=course)
        total_score = 0

        for question in course.questions.all():
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                submission.choices.add(choice)
                if choice.is_correct:
                    total_score += question.grade

        submission.score = total_score
        submission.save()

        return render(request, 'onlinecourse/exam_result.html', {
            'course': course,
            'submission': submission
        })

    return render(request, 'onlinecourse/exam.html', {'course': course})


@login_required
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    submission = Submission.objects.filter(user=request.user, course=course).last()

    return render(request, 'onlinecourse/exam_result.html', {
        'course': course,
        'submission': submission
    })
