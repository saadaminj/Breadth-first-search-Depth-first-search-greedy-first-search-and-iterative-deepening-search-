import sys
import queue
class graph:
    def __init__(self):
        self.dict={
            'Arad':['Zerind','Timisoara','Sibiu'],
            'Bucharest':['Fagaras','Giurgiu','Pitesti','Urziceni'],
            'Craiova':['Drobeta','Pitesti','Rimnicu Vilcea'],
            'Drobeta':['Craiova','Mehadia'],
            'Eforie':['Hirsova'],
            'Fagaras':['Bucharest','Sibiu'],
            'Giurgiu':['Bucharest'],
            'Hirsova':['Eforie','Urziceni'],
            'Lasi':['Neamt','Vaslui'],
            'Lugoj':['Mehadia','Timisoara'],
            'Mehadia':['Drobeta','Lugoj'],
            'Neamt':['Lasi'],
            'Oradea':['Sibiu','Zerind'],
            'Pitesti':['Bucharest','Craiova','Rimnicu Vilcea'],
            'Rimnicu Vilcea':['Craiova','Sibiu','Pitesti'],
            'Sibiu':['Oradea','Rimnicu Vilcea','Arad','Fagaras'],
            'Timisoara':['Arad','Lugoj'],
            'Urziceni':['Bucharest','Hirsova','Vaslui'],
            'Vaslui':['Urziceni','Lasi'],
            'Zerind':['Oradea','Arad']
        }
        self.weight={
            'Arad':[75,118,140],
            'Bucharest':[211,90,101,85],
            'Craiova':[120,138,146],
            'Drobeta':[120,75],
            'Eforie':[86],
            'Fagaras':[211,99],
            'Giurgiu':[90],
            'Hirsova':[86,98],
            'Lasi':[87,92],
            'Lugoj':[70,111],
            'Mehadia':[75,70],
            'Neamt':[87],
            'Oradea':[151,71],
            'Pitesti':[101,138,97],
            'Rimnicu Vilcea':[146,80,97],
            'Sibiu':[151,80,140,99],
            'Timisoara':[118,111],
            'Urziceni':[85,98,142],
            'Vaslui':[142,92],
            'Zerind':[71,75]
        }
        self.h={
            'Arad':366,
            'Bucharest':0,
            'Craiova':160,
            'Drobeta':242,
            'Eforie':161,
            'Fagaras':176,
            'Giurgiu':77,
            'Hirsova':151,
            'Lasi':226,
            'Lugoj':244,
            'Mehadia':241,
            'Neamt':234,
            'Oradea':380,
            'Pitesti':100,
            'Rimnicu Vilcea':193,
            'Sibiu':253,
            'Timisoara':329,
            'Urziceni':80,
            'Vaslui':199,
            'Zerind':374
        }
    def BFS(self,start,end):
        visited=[]
        q=[]
        path=[]
        cost=0
        f='null'
        for i in range(20):
            visited.append(False)
        q.append(start)
        while len(q)!=0:
            x=q.pop(0)
            if(f!="null"):
                try:
                    cost+=self.weight[f][list(self.dict[f]).index(x)]
                except:
                    None
            if(visited[list(self.dict.keys()).index(x)]==True):
                continue
            path.append(x)
            if(x==end):
                f = open("Q1output.txt", "a")
                f.write("BFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                f.close()
                print("BFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                return cost
            visited[list(self.dict.keys()).index(x)]=True
            for i in self.dict[x]:
                if(visited[list(self.dict.keys()).index(i)]==False):
                    q.append(i)
            f=x
        f = open("Q1output.txt", "a")
        f.write("BFS : Failed to reach Goal")
        f.close()
        print("BFS : Failed to reach Goal")
        return 0
    
    def GFS(self,start,end):
        visited=[]
        q=[]
        path=[]
        cost=0
        f='null'
        for i in range(20):
            visited.append(False)
        q.append(start)
        while len(q)!=0:
            x=q.pop(0)
            if(f!="null"):
                try:
                    cost+=self.weight[f][list(self.dict[f]).index(x)]
                except:
                    None
            if(visited[list(self.dict.keys()).index(x)]==True):
                continue
            path.append(x)
            if(x==end):
                f = open("Q1output.txt", "a")
                f.write("GFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                f.close()
                print("GFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                return cost
            visited[list(self.dict.keys()).index(x)]=True
            m=sys.maxsize
            for i in self.dict[x]:
                if(visited[list(self.dict.keys()).index(i)]==False):
                    if(m>self.h[i]):
                        m=self.h[i]
                        chosen=i
            if(m!=sys.maxsize):
                q.append(chosen)
            f=x
        f = open("Q1output.txt", "a")
        f.write("GFS : Failed to reach Goal")
        f.close()
        print("GFS : Failed to reach Goal")
        return 0
    def UCS(self,start,end):
        visited=[]                 
        q=queue.PriorityQueue()         
        q.put((0,start,[start]))               
        while not q.empty():             
            cost,x,path = q.get()
            visited.append(x)    
            if x==end:     
                f = open("Q1output.txt", "a")
                f.write("UFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                f.close()
                print("UCS : Cost = "+str(cost)+" Goal Reached "+str(path))
                return cost            
            else:
                for i in self.dict[x]:
                    if i not in visited:
                        q.put((cost+self.weight[x][list(self.dict[x]).index(i)],i,path+[i]))
        print("UFS : Failed to reach Goal")
        return 0
    def iDFS(self,start,end):
        for i in range(len(self.dict)):
            cost=self.DFS(start,end,i)
            if(cost):
                return cost
        f = open("Q1output.txt", "a")
        f.write("iDFS : Failed to reach Goal")
        f.close()
        print("iDFS : Failed to reach Goal")
        return 0
    def DFS(self,start,end,deep):
        visited=[]
        q=[]
        path=[]
        cost=0
        f='null'
        for i in range(20):
            visited.append(False)
        q.append(start)
        while len(q)!=0:
            x=q.pop()
            if(f!="null"):
                try:
                    cost+=self.weight[f][list(self.dict[f]).index(x)]
                except:
                    None
            if(visited[list(self.dict.keys()).index(x)]==True):
                continue
            path.append(x)
            if(len(path)>=deep):
                return 0;
            if(x==end):
                f = open("Q1output.txt", "a")
                f.write("iDFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                f.close()
                print("iDFS : Cost = "+str(cost)+" Goal Reached "+str(path))
                return cost;
                break
            visited[list(self.dict.keys()).index(x)]=True
            for i in self.dict[x]:
                if(visited[list(self.dict.keys()).index(i)]==False):
                    q.append(i)
            f=x
        
        f = open("Q1output.txt", "a")
        f.write("iDFS : Failed to reach Goal")
        f.close()
        print("iDFS : Failed to reach Goal")
        return 0

x=graph()
algo={
    'bfs':0,
    'gfs':0,
    'ucs':0,
    'idfs':0
}
#Bucharest
source=[]
dest=[]

f = open("Q1.txt","r");
lines = f.readlines();
for i in lines:
    thisline = i.split();
    source.append(thisline[0])
    dest.append(thisline[1],)

f = open("Q1output.txt", "w")
f.close()
for i in range(len(source)):
    f = open("Q1output.txt", "a")
    f.write("\n\n\n")
    f.write("Source : "+source[i]+"       Destination : "+dest[i]+"\n")
    f.close()
    print("\n\n\n")
    print("Source : "+source[i]+"       Destination : "+dest[i]+"\n")
    algo['bfs']=x.BFS(source[i],dest[i])
    algo['gfs']=x.GFS(source[i],dest[i])
    algo['ucs']=x.UCS(source[i],dest[i])
    algo['idfs']=x.iDFS(source[i],dest[i]) 

    try:
        f = open("Q1output.txt", "a")
        f.write("\nIN ASCENDING ORDER\n")
        f.write(print(sorted(algo.items(),key=lambda kv:(kv[1], kv[0]))))
        f.close()
        print("\nIN ASCENDING ORDER\n")
        print(sorted(algo.items(),key=lambda kv:(kv[1], kv[0])))
    except:
        None