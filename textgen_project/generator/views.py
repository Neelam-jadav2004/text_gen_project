from django.shortcuts import render
from .lstm_model import generate_text
from .models import GeneratedText

def home(request):
    output = ""

    if request.method == "POST":
        seed = request.POST.get("seed")
        output = generate_text(seed)

        GeneratedText.objects.create(
            seed_text=seed,
            output_text=output
        )

    return render(request, "index.html", {"output": output})


# Create your views here.
