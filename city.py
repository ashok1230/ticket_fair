class city:
    def __init__(self):
        import math
        stops={1:'majestic',2:'corporation',3:'hudson',4:'shanti nagar',5:'wilson garden',
                6:'nimhans',7:'dairy circle',8:'forum',9:'adugodi',10:'st.johns'}
        fair={1:4,2:6,3:8,4:10,5:11,6:13,7:14,8:15,9:16}
        source=int(raw_input("enter source station: "))
        destination=int(raw_input("enter destination station: "))
        number=int(raw_input("enter number of tickets:"))
        diff_stop=int(math.fabs(source-destination))
        print 'Ticket from ',stops[source],'to ',stops[destination]
        print 'fair for 1 ticket',fair[diff_stop]
        print 'total fair=',fair[diff_stop]*number
        
a=city()
