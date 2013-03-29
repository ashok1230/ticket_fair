class ticket:
    def __init__(self):
        import math
        stops={1:'hyderabad',2:'rangareddy',3:'nizamabad',4:'kurnool',5:'nandyala',
                6:'kadapa',7:'rajampet',8:'kodur',9:'renigunta',10:'tirupathi'}
        dist_from_hyd={1:0,2:39,3:157,4:276,5:301,6:399,7:476,8:532,9:600,10:615}
        source=int(raw_input("enter source station: "))
        destination=int(raw_input("enter destination station: "))
        number=int(raw_input("enter number of tickets:"))
        if source==1:
            dist=dist_from_hyd[destination]
        else:
            dist=dist_from_hyd[destination]-dist_from_hyd[source]
        
        distance=int(math.fabs(dist))
        print 'Distance :',distance
        fair=distance*1.2
        total_fair=int(number*fair)
        print 'Fair from',stops[source],'to',stops[destination],':',fair
        print 'Total fair:',total_fair

a=ticket()
