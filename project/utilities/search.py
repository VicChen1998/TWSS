from project.models import GlobalValue


# DO NOT TOUCH THESE FUCKING CODE !
# DO NOT TOUCH THESE FUCKING CODE !
# DO NOT TOUCH THESE FUCKING CODE !

# 我自己都讲不清这边是怎么运行的了

# BUT IT JUST FUCKING WORK !
# BUT IT JUST FUCKING WORK !
# BUT IT JUST FUCKING WORK !

# 本项目两万行代码我只怕这一百行

# VIC CHEN 2017.9.12


#                             _ooOoo_
#                            o8888888o
#                            88" . "88
#                            (| -_- |)
#                            O\  =  /O
#                         ____/`---'\____
#                       .'  \\|     |//  `.
#                      /  \\|||  :  |||//  \
#                     /  _||||| -:- |||||-  \
#                     |   | \\\  -  /// |   |
#                     | \_|  ''\---/''  |   |
#                     \  .-\__  `-`  ___/-. /
#                   ___`. .'  /--.--\  `. . __
#                ."" '<  `.___\_<|>_/___.'  >'"".
#               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#               \  \ `-.   \_ __\ /__ _/   .-` /  /
#          ======`-.____`-.___\_____/___.-`____.-'======
#                             `=---='
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                     佛祖保佑        永无BUG

# TODO: 可简化 合并

def search(request, cource_list):

    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data'].split(',')[0]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        cource_list = cource_list.filter(year=year)

    semester = ''
    if 'location_semester_post' in request.POST:
        semester = request.POST['location_semester_post']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        semester = request.POST['extra_data'].split(',')[1]
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        cource_list = cource_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    return cource_list, year, semester


def audit_search(request, cource_list):
    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        elif year != u'所有':
            cource_list = cource_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            cource_list = cource_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data'].split(',')[0]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        cource_list = cource_list.filter(year=year)

    semester = ''
    if 'location_semester_post' in request.POST:
        semester = request.POST['location_semester_post']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        semester = request.POST['extra_data'].split(',')[1]
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        cource_list = cource_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    audit_status = ''
    if 'location_audit_status_post' in request.POST:
        audit_status = request.POST['location_audit_status_post']
        if audit_status == u'所有':
            pass
        if audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=0)
        if audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        if audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=2)
    elif 'audit_status' in request.POST:
        audit_status = request.POST['audit_status']
        if audit_status == u'所有':
            pass
        if audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=0)
        if audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        if audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=2)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        audit_status = request.POST['extra_data'].split(',')[2]
        if audit_status == u'所有':
            pass
        if audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=0)
        if audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        if audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=2)
    else:
        audit_status = u'所有'

    return cource_list, year, semester, audit_status