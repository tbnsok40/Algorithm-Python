large = ['A00', 'A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11']
large = []
for j in range(0, 12):
    if j < 10:
        large.append('A0' + str(j))
    else:
        large.append('A' + str(j))
# print(large)
medium = ['E00', 'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28', 'E29', 'E30', 'E31', 'E32', 'E33', 'E34', 'E35', 'E36', 'E37', 'E38', 'E39', 'E40', 'E41', 'E42', 'E43', 'E44', 'E45', 'E46', 'E47', 'E48', 'E49', 'E50', 'E51', 'E52', 'E53', 'E54', 'E55']

for k in range(0, 56):
    if k < 10:
        medium.append('E0' + str(k))
    else:
        medium.append('E' + str(k))
# print(medium)

small = ['F000', 'F001', 'F002', 'F003', 'F004', 'F005', 'F006', 'F007', 'F008', 'F009', 'F010', 'F011', 'F012', 'F013', 'F014', 'F015', 'F016', 'F017', 'F018', 'F019', 'F020', 'F021', 'F022', 'F023', 'F024', 'F025', 'F026', 'F027', 'F028', 'F029', 'F030', 'F031', 'F032', 'F033', 'F034', 'F035', 'F036', 'F037', 'F038', 'F039', 'F040', 'F041', 'F042', 'F043', 'F044', 'F045', 'F046', 'F047', 'F048', 'F049', 'F050', 'F051', 'F052', 'F053', 'F054', 'F055', 'F056', 'F057', 'F058', 'F059', 'F060', 'F061', 'F062', 'F063', 'F064', 'F065', 'F066', 'F067', 'F068', 'F069', 'F070', 'F071', 'F072', 'F073', 'F074', 'F075', 'F076', 'F077', 'F078', 'F079', 'F080', 'F081', 'F082', 'F083', 'F084', 'F085', 'F086', 'F087', 'F088', 'F089', 'F090', 'F091', 'F092', 'F093', 'F094', 'F095', 'F096', 'F097', 'F098', 'F099', 'F100', 'F101', 'F102', 'F103', 'F104', 'F105', 'F106', 'F107', 'F108', 'F109', 'F110', 'F111', 'F112', 'F113', 'F114', 'F115', 'F116', 'F117', 'F118', 'F119', 'F120', 'F121', 'F122', 'F123', 'F124', 'F125', 'F126', 'F127', 'F128', 'F129', 'F130', 'F131', 'F132', 'F133', 'F134', 'F135', 'F136', 'F137', 'F138', 'F139', 'F140', 'F141', 'F142', 'F143', 'F144', 'F145', 'F146', 'F147', 'F148', 'F149', 'F150', 'F151', 'F152', 'F153', 'F154', 'F155', 'F156', 'F157', 'F158', 'F159', 'F160', 'F161', 'F162', 'F163', 'F164', 'F165', 'F166', 'F167', 'F168', 'F169', 'F170', 'F171', 'F172', 'F173', 'F174', 'F175', 'F176', 'F177', 'F178', 'F179', 'F180', 'F181', 'F182', 'F183', 'F184', 'F185', 'F186', 'F187', 'F188', 'F189', 'F190', 'F191', 'F192', 'F193', 'F194', 'F195', 'F196', 'F197', 'F198', 'F199', 'F200', 'F201', 'F202', 'F203', 'F204', 'F205', 'F206', 'F207', 'F208', 'F209', 'F210']
for i in range(0,211):
    if i < 10:
        small.append('F00' + str(i))
    elif i >= 10 and i < 100:
        small.append('F0' + str(i))
    else:
        small.append('F' + str(i))
# print(small)



medium_key = ['의정부지방법원',
'고양지원',
'인천지방법원',
'부천지원',
'춘천지방법원',
'강릉지원',
'원주지원',
'속초지원',
'영월지원',
'수원지방법원',

'성남지원',
'안산지원',
'평택지원',
'여주지원',
'안양지원',
'대전지방법원',
'홍성지원',
'공주지원',
'논산지원',
'서산지원',

'천안지원',
'청주지방법원',
'충주지원',
'제천지원',
'영동지원',
'대구지방법원',
'대구서부지원',
'안동지원',
'경주지원',
'포항지원',

'김천지원',
'상주지원',
'의성지원',
'영덕지원',
'부산지방법원',
'부산동부지원',
'부산서부지원',
'울산지방법원',
'창원지방법원',
'마산지원',

'진주지원',
'통영지원',
'밀양지원',
'거창군',
'광주지방법원',
'목포지원',
'장흥지원',
'순천지원',
'해남지원',
'전주지방법원',

'군산지원',
'정읍지원',
'남원지원',
'제주지방법원']
# print(len(medium_key))
medium = ['E00', 'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28', 'E29', 'E30', 'E31', 'E32', 'E33', 'E34', 'E35', 'E36', 'E37', 'E38', 'E39', 'E40', 'E41', 'E42', 'E43', 'E44', 'E45', 'E46', 'E47', 'E48', 'E49', 'E50', 'E51', 'E52', 'E53']
# print(len(medium))
medium_dict = {}
for key, value in zip(medium, medium_key):
    medium_dict[key] = value

# print(medium_dict)

##################################################################################################

towns = ['강남구',
'관악구',
'동작구',
'서초구',
'종로구',
'중구',
'성동구',
'광진구',
'강동구',
'송파구',
'강서구',
'양천구',
'영등포구',
'구로구',
'금천구',
'도봉구',
'강북구',
'노원구',
'동대문구',
'성북구',
'중랑구',
'마포구',
'서대문구',
'은평구',
'용산구',
'의정부시',
'양주시',
'동두천시',
'포천시',
'남양주시',
'구리시',
'가평군',
'연천군',
'철원군',
'고양시',
'파주시',
'인천광역시 전지역',
'부천시',
'김포시',
'춘천시',
'화천군',
'양구군',
'인제군',
'홍천군',
'강릉시',
'삼척시',
'동해시',
'원주시',
'횡성군',
'속초시',
'고성군',
'양양군',
'태백시',
'영월군',
'평창군',
'정선군',
'수원시',
'용인시',
'오산시',
'화성시',
'성남시',
'하남시',
'광주시',
'안산시',
'광명시',
'시흥시',
'평택시',
'안성시',
'이천시',
'여주시',
'양평군',
'안양시',
'군포시',
'의왕시',
'과천시',
'대전광역시 전지역',
'세종특별자치시',
'금산군',
'홍성군',
'예산군',
'보령시',
'서천군',
'공주시',
'청양군',
'논산시',
'계룡시',
'부여군',
'서산시',
'당진시',
'태안군',
'천안시',
'아산시',
'청주시',
'괴산군',
'진천군',
'보은군',
'증평군',
'충주시',
'음성군',
'제천시',
'단양군',
'영동군',
'옥천군',
'중구',
'동구',
'북구',
'남구',
'수성구',
'경산시',
'영천시',
'칠곡군',
'청도군',
'서구',
'달서구',
'달성군',
'성주군',
'고령군',
'안동시',
'영주시',
'봉화군',
'경주시',
'포항시',
'울릉군',
'김천시',
'구미시',
'상주시',
'문경시',
'예천군',
'의성군',
'군위군',
'청송군',
'영덕군',
'울진군',
'영양군',
'중구',
'동구',
'동래구',
'연제구',
'부산진구',
'금정구',
'영도구',
'남구',
'해운대구',
'수영구',
'기장군',
'서구',
'북구',
'사상구',
'사하구',
'강서구',
'울산광역시 전지역',
'양산시',
'창원시 성산구',
'의창구',
'진해구',
'김해시',
'창원시 마산회원구',
'마산시 합포구',
'함안군',
'의령군',
'진주시',
'사천시',
'산청군',
'하동군',
'남해군',
'통영시',
'거제시',
'고성군',
'밀양시',
'창녕군',
'거창군',
'함양군',
'합천군',
'광주광역시전지역',
'나주시',
'화순군',
'영광군',
'장성군',
'담양군',
'곡성군',
'목포시',
'신안군',
'무안군',
'함평군',
'영암군',
'장흥군',
'강진군',
'순천시',
'광양시',
'여수시',
'구례군',
'보성군',
'고흥군',
'해남군',
'진도군',
'완도군',
'전주시',
'김제시',
'완주군',
'임실군',
'진안군',
'무주군',
'군산시',
'익산시',
'정읍시',
'고창군',
'부안군',
'남원시',
'장수군',
'순창군',
'제주특별자치도']
small_key = {}
for k, v in zip(small, towns):
    small_key[k] = v



print(small_key)





list1= [1,6,7,3,2]
print(list1.sort())
print(sorted(list1))


dict2 = {}

dict2['a'] = 1
dict2['b'] = 2
print(dict2['a'])


string = '1234321'
print(string.split('4'))

print(string.count('3'))

if score >= 91:
    print("grade is A")
elif 90 >= score and score >= 81:
    print("grade is B")
else:
    print("grade is C")