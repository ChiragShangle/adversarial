from django.shortcuts import render

from django.http import HttpResponse


def evasion(request):
    model=None
    attack=None
    original_image1='king_penguin: 99.80%'
    adversarial_image1=None
     
    adversarial_image2=None
     
    adversarial_image3=None
     
    adversarial_image4=None
     
    adversarial_image5=None
     
    adversarial_image6=None
     
    adversarial_image7=None
    if request.method == 'POST':
        model = request.POST.get('model')
        attack = request.POST.get('attack')
    if model == 'DenseNet':
        if attack == 'FGSM':
            original_image1='king_penguin: 99.80%'
            adversarial_image1='king_penguin: 99.80%'
             
            adversarial_image2='king_penguin: 79.42%'
             
            adversarial_image3='king_penguin: 58.41%'
             
            adversarial_image4='king_penguin: 47.54%'
             
            adversarial_image5='king_penguin: 37.20%'
             
            adversarial_image6='king_penguin: 24.39%'
             
            adversarial_image7='torch: 17.06%' 
        elif attack == 'BIM':
            original_image1='king_penguin: 99.80%'
            adversarial_image1='king_penguin: 99.80%'
            adversarial_image2='ptarmigan: 87.80%'
            adversarial_image3='ski: 99.96%'
             
            adversarial_image4='crutch: 100.00%'
             
            adversarial_image5='crutch: 100.00%'
             
            adversarial_image6='pajama: 100.00%'
             
            adversarial_image7='pajama: 100.00%'  
        elif attack == 'DEEPFOOL':
            original_image1='king_penguin: 99.80%'
            adversarial_image1='king_penguin: 95.75%'
             
            adversarial_image2='king_penguin: 94.19%'
             
            adversarial_image3='king_penguin: 93.02%'
             
            adversarial_image4='king_penguin: 90.15%'
             
            adversarial_image5='king_penguin: 88.70%'
             
            adversarial_image6='king_penguin: 80.29%'
             
            adversarial_image7='king_penguin: 75.70%'  
        elif attack == 'PGD':
            original_image1='king_penguin: 99.80%'
            adversarial_image1='king_penguin: 99.80%'
             
            adversarial_image2='ski: 95.33%'
             
            adversarial_image3='ski: 99.99%'
             
            adversarial_image4='crutch: 100.00%'
             
            adversarial_image5='crutch: 100.00%'
             
            adversarial_image6='pajama: 100.00%'
             
            adversarial_image7='pajama: 100.00%'  
        # elif attack == 'C&W':
        #     original_image1='king_penguin: 99.80%'
        #     adversarial_image1=None
             
        #     adversarial_image2=None
             
        #     adversarial_image3=None
             
        #     adversarial_image4=None
             
        #     adversarial_image5=None
             
        #     adversarial_image6=None
             
        #     adversarial_image7=None 
    elif model == 'EfficientNetB0':
        if attack == 'FGSM':
            original_image1='king_penguin: 98.09%'
            adversarial_image1='king_penguin: 98.09%'
             
            adversarial_image2='king_penguin: 98.08%'
             
            adversarial_image3='king_penguin: 98.08%'
             
            adversarial_image4='king_penguin: 98.07%'
             
            adversarial_image5='king_penguin: 98.07%'
             
            adversarial_image6='king_penguin: 98.07%'
             
            adversarial_image7='king_penguin: 98.06%'   
        elif attack == 'BIM':
            original_image1='king_penguin: 98.09%'
            adversarial_image1='king_penguin: 98.09%'
                 
            adversarial_image2='king_penguin: 96.63%'
                 
            adversarial_image3='king_penguin: 94.76%'
                 
            adversarial_image4='king_penguin: 92.65%'
                 
            adversarial_image5='king_penguin: 90.38%'
                 
            adversarial_image6='king_penguin: 87.89%'
                 
            adversarial_image7='king_penguin: 85.04%' 

        elif attack == 'PGD':
            original_image1='king_penguin: 98.09%'
            adversarial_image1='king_penguin: 98.09%'
             
            adversarial_image2='king_penguin: 96.63%'
             
            adversarial_image3='king_penguin: 94.76%'
             
            adversarial_image4='king_penguin: 92.65%'
             
            adversarial_image5='king_penguin: 90.38%'
             
            adversarial_image6='king_penguin: 87.79%'
             
            adversarial_image7='king_penguin: 84.54%' 
        elif attack == 'DEEPFOOL':
            original_image1='king_penguin: 98.09%'
            adversarial_image1='king_penguin: 98.09%'
             
            adversarial_image2='coho: 21.40%'
             
            adversarial_image3='coho: 23.20%'
             
            adversarial_image4='coho: 24.77%'
             
            adversarial_image5='coho: 26.13%'
             
            adversarial_image6='coho: 27.29%'
             
            adversarial_image7='coho: 28.27%'  
        # elif attack == 'C&W':
        #     original_image1='king_penguin: 99.80%'
        #     adversarial_image1=None
             
        #     adversarial_image2=None
             
        #     adversarial_image3=None
             
        #     adversarial_image4=None
             
        #     adversarial_image5=None
             
        #     adversarial_image6=None
             
        #     adversarial_image7=None 
    elif model == 'EfficientNetB7':
            if attack == 'FGSM':
                original_image1='king_penguin: 84.97%'
                adversarial_image1='king_penguin: 84.97%'
                 
                adversarial_image2='king_penguin: 84.97%'
                 
                adversarial_image3='king_penguin: 84.97%'
                 
                adversarial_image4='king_penguin: 84.97%'
                 
                adversarial_image5='king_penguin: 84.97%'
                 
                adversarial_image6='king_penguin: 84.96%'
                 
                adversarial_image7='king_penguin: 84.96%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 84.97%'
                adversarial_image1='king_penguin: 84.97%'
                 
                adversarial_image2='king_penguin: 82.82%'
                 
                adversarial_image3='king_penguin: 80.11%'
                 
                adversarial_image4='king_penguin: 78.79%'
                 
                adversarial_image5='king_penguin: 77.60%'
                 
                adversarial_image6='king_penguin: 75.55%'
                 
                adversarial_image7='king_penguin: 73.02%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 84.97%'
                adversarial_image1='king_penguin: 84.97%'
                 
                adversarial_image2='king_penguin: 82.83%'
                 
                adversarial_image3='king_penguin: 80.16%'
                 
                adversarial_image4='king_penguin: 76.99%'
                 
                adversarial_image5='king_penguin: 75.26%'
                 
                adversarial_image6='king_penguin: 74.98%'
                 
                adversarial_image7='king_penguin: 71.96%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 91.05%'
                 
                adversarial_image2='king_penguin: 91.01%'
                 
                adversarial_image3='king_penguin: 90.55%'
                 
                adversarial_image4='king_penguin: 87.77%'
                 
                adversarial_image5='king_penguin: 80.67%'
                 
                adversarial_image6='king_penguin: 72.29%'
                 
                adversarial_image7='king_penguin: 66.21%'   
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'InceptionV3':
            if attack == 'FGSM':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 86.97%'
                 
                adversarial_image2='king_penguin: 71.97%'
                 
                adversarial_image3='king_penguin: 77.93%'
                 
                adversarial_image4='king_penguin: 82.09%'
                 
                adversarial_image5='king_penguin: 79.64%'
                 
                adversarial_image6='king_penguin: 81.48%'
                 
                adversarial_image7='king_penguin: 83.99%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 86.97%'
                 
                adversarial_image2='king_penguin: 33.72%'
                 
                adversarial_image3='lab_coat: 32.00%'
                 
                adversarial_image4='groom: 99.76%'
                 
                adversarial_image5='shower_curtain: 98.38%'
                 
                adversarial_image6='stage: 99.19%'
                 
                adversarial_image7='tray: 42.38%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 86.97%'
                 
                adversarial_image2='king_penguin: 19.04%'
                 
                adversarial_image3='groom: 97.77%'
                 
                adversarial_image4='jigsaw_puzzle: 100.00%'
                 
                adversarial_image5='microphone: 99.99%'
                 
                adversarial_image6='jigsaw_puzzle: 100.00%'
                 
                adversarial_image7='quill: 100.00%  '  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 91.05%'
                 
                adversarial_image2='king_penguin: 91.01%'
                 
                adversarial_image3='king_penguin: 90.55%'
                 
                adversarial_image4='king_penguin: 87.77%'
                 
                adversarial_image5='king_penguin: 80.67%'
                 
                adversarial_image6='king_penguin: 72.29%'
                 
                adversarial_image7='king_penguin: 66.21%'  
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'MobileNet':
            if attack == 'FGSM':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.99%'
                
                adversarial_image2='ptarmigan: 14.89%'
                
                adversarial_image3='paper_towel: 15.48%'
                
                adversarial_image4='paper_towel: 8.23%'
                
                adversarial_image5='sea_snake: 12.74%'
                
                adversarial_image6='sea_snake: 20.81%'
                
                adversarial_image7='sea_snake: 17.59%'
            elif attack == 'BIM':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.99%'
                 
                adversarial_image2='ski: 99.32%'
                 
                adversarial_image3='radiator: 99.99%'
                 
                adversarial_image4='radiator: 99.99%'
                 
                adversarial_image5='radiator: 100.00%'
                 
                adversarial_image6='screw: 100.00%'
                 
                adversarial_image7='screw: 100.00%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.99%'
                 
                adversarial_image2='ski: 99.14%'
                 
                adversarial_image3='radiator: 99.99%'
                 
                adversarial_image4='radiator: 100.00%'
                 
                adversarial_image5='radiator: 100.00%'
                 
                adversarial_image6='screw: 100.00%'
                 
                adversarial_image7='screw: 100.00%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.92%'
                 
                adversarial_image2='king_penguin: 99.88%'
                 
                adversarial_image3='king_penguin: 99.82%'
                 
                adversarial_image4='king_penguin: 99.74%'
                 
                adversarial_image5='king_penguin: 99.66%'
                 
                adversarial_image6='king_penguin: 99.37%'
                 
                adversarial_image7='king_penguin: 98.86%'  
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'NasNet':
            if attack == 'FGSM':
                original_image1='king_penguin: 99.80%'
                adversarial_image1='king_penguin: 94.17%'
                 
                adversarial_image2='king_penguin: 93.72%'
                 
                adversarial_image3='king_penguin: 92.95%'
                 
                adversarial_image4='king_penguin: 91.17%'
                 
                adversarial_image5='king_penguin: 90.79%'
                 
                adversarial_image6='king_penguin: 81.97%'
                 
                adversarial_image7='king_penguin: 78.25%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 99.80%'
                adversarial_image1='hair_slide: 3.42%'
                 
                adversarial_image2='hair_slide: 3.38%'
                 
                adversarial_image3='hair_slide: 3.33%'
                 
                adversarial_image4='hair_slide: 3.29%'
                 
                adversarial_image5='hair_slide: 3.25%'
                 
                adversarial_image6='hair_slide: 3.21%'
                 
                adversarial_image7='hair_slide: 3.18%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 91.17%'
                adversarial_image1='king_penguin: 91.17%'
                 
                adversarial_image2='king_penguin: 91.11%'
                 
                adversarial_image3='binoculars: 89.24%'
                 
                adversarial_image4='pajama: 94.03%'
                 
                adversarial_image5='cowboy_boot: 81.85%'
                 
                adversarial_image6='bluetick: 93.58%'
                 
                adversarial_image7='sock: 98.27%' 
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.92%'
                 
                adversarial_image2='king_penguin: 99.88%'
                 
                adversarial_image3='king_penguin: 99.82%'
                 
                adversarial_image4='king_penguin: 99.74%'
                 
                adversarial_image5='king_penguin: 99.66%'
                 
                adversarial_image6='king_penguin: 99.37%'
                 
                adversarial_image7='king_penguin: 98.86%'
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'ResNet50':
            if attack == 'FGSM':
                original_image1='king_penguin: 97.74%'
                adversarial_image1='king_penguin: 97.74%'
                 
                adversarial_image2='king_penguin: 97.72%'
                 
                adversarial_image3='king_penguin: 97.71%'
                 
                adversarial_image4='king_penguin: 97.69%'
                 
                adversarial_image5='king_penguin: 97.68%'
                 
                adversarial_image6='king_penguin: 97.67%'
                 
                adversarial_image7='king_penguin: 97.66%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 99.99%'
                adversarial_image1='king_penguin: 99.99%'
                 
                adversarial_image2='ski: 99.32%'
                 
                adversarial_image3='radiator: 99.99%'
                 
                adversarial_image4='radiator: 99.99%'
                 
                adversarial_image5='radiator: 100%'
                 
                adversarial_image6='screw: 100.00%'
                 
                adversarial_image7='screw: 100.00%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 75.11%'
                adversarial_image1='king_penguin: 97.74%'
                 
                adversarial_image2='king_penguin: 89.44%'
                 
                adversarial_image3='king_penguin: 60.64%'
                 
                adversarial_image4='lab_coat: 37.53%'
                 
                adversarial_image5='lab_coat: 64.08%'
                 
                adversarial_image6='bluetick: 93.58%'
                 
                adversarial_image7='sock: 98.27%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 86.97%'
                adversarial_image1='king_penguin: 91.05%'
                 
                adversarial_image2='king_penguin: 90.01%'
                 
                adversarial_image3='king_penguin: 89.55%'
                 
                adversarial_image4='king_penguin: 87.77%'
                 
                adversarial_image5='king_penguin: 78.67%'
                 
                adversarial_image6='king_penguin: 62.29%'
                 
                adversarial_image7='king_penguin: 56.21%'  
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'VGG16':
            if attack == 'FGSM':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 100.00%'
                 
                adversarial_image3='king_penguin: 100.00%'
                 
                adversarial_image4='king_penguin: 100.00%'
                 
                adversarial_image5='king_penguin: 100.00%'
                 
                adversarial_image6='king_penguin: 100.00%'
                 
                adversarial_image7='king_penguin: 100.00%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 100.00%'
                 
                adversarial_image3='king_penguin: 100.00%'
                 
                adversarial_image4='king_penguin: 100.00%'
                 
                adversarial_image5='king_penguin: 99.99%'
                 
                adversarial_image6='king_penguin: 99.98%'
                 
                adversarial_image7='king_penguin: 99.95%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 99.96%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 100.00%'
                 
                adversarial_image3='king_penguin: 100.00%'
                 
                adversarial_image4='king_penguin: 100.00%'
                 
                adversarial_image5='king_penguin: 99.99%'
                 
                adversarial_image6='king_penguin: 99.98%'
                 
                adversarial_image7='king_penguin: 99.94%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='king_penguin: 99.96%'
                adversarial_image2='king_penguin: 99.88%'
                 
                adversarial_image3='king_penguin: 99.82%'
                 
                adversarial_image4='king_penguin: 99.74%'
                 
                adversarial_image5='king_penguin: 99.66%'
                 
                adversarial_image6='king_penguin: 99.37%'
                 
                adversarial_image7='king_penguin: 98.86%' 
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'VGG19':
            if attack == 'FGSM':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 100.00%'
                 
                adversarial_image3='king_penguin: 100.00%'
                 
                adversarial_image4='king_penguin: 100.00%'
                 
                adversarial_image5='king_penguin: 100.00%'
                 
                adversarial_image6='king_penguin: 100.00%'
                 
                adversarial_image7='king_penguin: 100.00%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 99.99%'
                 
                adversarial_image3='king_penguin: 99.99%'
                 
                adversarial_image4='king_penguin: 99.97%'
                 
                adversarial_image5='king_penguin: 99.92%'
                 
                adversarial_image6='king_penguin: 99.81%'
                 
                adversarial_image7='king_penguin: 99.54%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 99.96%'
                adversarial_image1='king_penguin: 100.00%'
                 
                adversarial_image2='king_penguin: 99.99%'
                 
                adversarial_image3='king_penguin: 99.99%'
                 
                adversarial_image4='king_penguin: 99.97%'
                 
                adversarial_image5='king_penguin: 99.92%'
                 
                adversarial_image6='king_penguin: 99.80%'
                 
                adversarial_image7='king_penguin: 99.49%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 100.00%'
                adversarial_image1='megalith: 20.42%'
                adversarial_image2='megalith: 18.97%'
                adversarial_image3='megalith: 17.32%'
                adversarial_image4='megalith: 15.58%'
                adversarial_image5='megalith: 14.13%'
                adversarial_image6='megalith: 13.06%'
                adversarial_image7='space_shuttle: 13.98%' 
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
    elif model == 'Xception':
            if attack == 'FGSM':
                original_image1='king_penguin: 90.61%'
                adversarial_image1='king_penguin: 90.61%'
                 
                adversarial_image2='king_penguin: 20.27%'
                 
                adversarial_image3='king_penguin: 5.31%'
                 
                adversarial_image4='sock: 4.05%'
                 
                adversarial_image5='maillot: 4.74%'
                 
                adversarial_image6='maillot: 4.74%'
                 
                adversarial_image7='maillot: 7.95%'   
            elif attack == 'BIM':
                original_image1='king_penguin: 90.61%'
                adversarial_image1='king_penguin: 90.61%'
                 
                adversarial_image2='coho: 77.96%'
                 
                adversarial_image3='lab_coat: 99.82%'
                 
                adversarial_image4='apron: 99.84%'
                 
                adversarial_image5='suit: 98.47%'
                 
                adversarial_image6='apron: 100.00%'
                 
                adversarial_image7='apron: 100.00%'  
            elif attack == 'PGD':
                original_image1='king_penguin: 90.61%'
                adversarial_image1='king_penguin: 90.61%'
                 
                adversarial_image2='coho: 96.23%'
                 
                adversarial_image3='lab_coat: 99.92%'
                 
                adversarial_image4='apron: 100.00%'
                 
                adversarial_image5='apron: 100.00%'
                 
                adversarial_image6='apron: 100.00%'
                 
                adversarial_image7='apron: 100.00%'  
            elif attack == 'DEEPFOOL':
                original_image1='king_penguin: 90.61%'
                adversarial_image1='king_penguin: 58.25%'
                 
                adversarial_image2='king_penguin: 59.35%'
                 
                adversarial_image3='king_penguin: 57.92%'
                 
                adversarial_image4='king_penguin: 52.16%'
                 
                adversarial_image5='king_penguin: 45.26%'
                 
                adversarial_image6='king_penguin: 35.50%'
                 
                adversarial_image7='king_penguin: 24.87%'  
            # elif attack == 'C&W':
            #     original_image1='king_penguin: 99.80%'
            #     adversarial_image1=None
                 
            #     adversarial_image2=None
                 
            #     adversarial_image3=None
                 
            #     adversarial_image4=None
                 
            #     adversarial_image5=None
                 
            #     adversarial_image6=None
                 
            #     adversarial_image7=None  
            

    return render(request,"evasion.html",{'model':model , 'attack':attack, 'original_image1':original_image1, 'adversarial_image1':adversarial_image1, 'adversarial_image2':adversarial_image2, 'adversarial_image3':adversarial_image3,  'adversarial_image4':adversarial_image4, 'adversarial_image5':adversarial_image5,'adversarial_image6':adversarial_image6, 'adversarial_image7':adversarial_image7})


def homepage(request):
    return render(request,"homepage.html")
def robustness(request):
    return render(request,"robustness.html")
