templates = ["Dear Parents This is to inform you that School will remain closed {#var#} on the occasion of {#var#} and School will reopen on {#var#}. Regards {#var#} Edu RBS",
             "{#var#} Dear Parents & Guardians, It is to inform you all that Parent Teacher Meeting for{#var#}{#var#} is scheduled on {#var#} Timing-. {#var#}. Regards {#var#} Edu RBS {#var#}",
             "Dear Parents & Guardians, It is hereby informed that {#var#}{#var#} You are requested to come to School {#var#} For any query call on {#var#}. Regards {#var#} Edu RBS",
             "Dear Parents & Guardian, It is hereby informed to you all that School is going to organize {#var#} for {#var#} So, it is mandatory for all the Students to be present along with {#var#}.Regards {#var#} Edu RBS",
             "Dear Parent, This is to inform you that School {#var#}{#var#} and will reopen on {#var#}.Regards {#var#} Edu RBS",
             "Dear Parents & Guardians, It is to inform you all that New School timing from {#var#} will be {#var#}.Regards {#var#} , Edu RBS"]

msg = "Good morning Dear Parents & Guardians, It is to inform you all that Parent Teacher Meeting for copy checking is scheduled on July 16, 2023 Timing-. 9am to 12am. Regards Principal Edu RBS nitin tripathi"

msg_words_lst= msg.replace(" "," ").split(' ')
#print(msg_words_lst)
match_count = []

for template in templates:
    count = 0
    for word in msg_words_lst:
        if word in template:
            count += 1
    match_count.append(count)
    count = 0

index = match_count.index(max(match_count))
probable_template = templates[index]

template_words_lst = probable_template.replace(" "," ").split(" ")
#print(template_words_lst)

#---------------------------------------------------------------after probable template is found------------------------------------------------------------------------------------------------------

i = 0
j = 0
matched = False

while (j < len(template_words_lst)) and (i < len(msg_words_lst)):
    if template_words_lst[j] == '{#var#}' or template_words_lst[j] == '{#var#}.' or template_words_lst[j] == '{#var#},' or template_words_lst[j].__contains__('{#var#}'):
        isVar = True
    else:
        isVar = False

    if isVar == False:
        if msg_words_lst[i] == template_words_lst[j]:
            matched = True
        else:
            matched = False
            print("No template matched.")
            break
        i+=1
        j+=1
    if isVar == True:
        if j == len(template_words_lst) - 1:                   #var in the end of template
            break
        if template_words_lst[j+1] == msg_words_lst[i]:
            matched = True
            isVar = False
            i += 1
            j += 2
        else:
            i += 1
            matched = False
if matched:
    print("Template found:")
    print(probable_template)

    

