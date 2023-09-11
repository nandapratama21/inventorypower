from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A',
        '1x1':'Nama',
        '1x2':'Harga',
        '1x3':'Kapasitas',
        '2x1':'Mie Ayam',
        '2x2':'Rp 18000',
        '2x3':'20',
        '3x1':'Ayam Bakar',
        '3x2':'Rp 18000',
        '3x3':'10',
        '4x1':'Nasi Alo',
        '4x2':'Rp 15000',
        '4x3':'15',
    }

    return render(request, "main.html", context)