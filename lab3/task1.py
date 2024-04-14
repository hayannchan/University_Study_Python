class Point():
    """класс точка на плоскости"""
    x,y = 0,0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class InvalidFigureError(Exception):
    """исключение, вызываемое при вводе некорректной фигуры (например совпадают точки)"""
    pass

def distance(p1,p2):
    """находит расстояние между двумя точками"""
    if not isinstance(p1,Point) or not isinstance(p2,Point):
        raise TypeError("Points should have Point type")
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**(0.5)

def isOnOneLine(p1, p2, p3):
    """проверяет, лежат ли 3 точки на одной прямой"""
    if not isinstance(p1,Point) or not isinstance(p2,Point) or not isinstance(p3,Point):
        raise TypeError("Points should have Point type")
    if (p3.x - p1.x)*(p2.y - p1.y) == (p3.y - p1.y)*(p2.x - p1.x):
        return True
    return False

def isParallel(p1,p2,p3,p4):
    """проверяет, являются ли прямая, проходящая через точки p1, p2 и прямая через точки p3,p4 параллельными"""
    if not isinstance(p1,Point) or not isinstance(p2,Point) or not isinstance(p3,Point) or not isinstance(p4,Point):
        raise TypeError("Points should have Point type")
    A1 = (p2.y - p1.y)
    B1 = (p1.x - p2.x)
    A2 = (p4.y - p3.y)
    B2 = (p3.x - p4.x)
    if (A1*B2==A2*B1):
        return True
    return False

class Rectangle():
    """класс прямоугольник"""
    listPoints = []
    def __init__(self, listPoints):
        if not isinstance(listPoints, list):
            raise TypeError("listPoints should have list type")
        if len(listPoints) != 4:
            raise TypeError("listPoints should have 4 elements")
        pointsSet = set()
        for e in listPoints:
            if not isinstance(e,Point):
                raise TypeError("Points should have Point type")
            pointsSet.add((e.x,e.y))
        if len(pointsSet) != 4:
            raise InvalidFigureError("Invalid rect") 
        for i in range(len(listPoints)):
            for j in range(i+1,len(listPoints)):
                for k in range(j+1,len(listPoints)):
                    if isOnOneLine(listPoints[i],listPoints[j],listPoints[k]):
                        print(i,j,k)
                        raise InvalidFigureError("Invalid rect") 
        if not isParallel(listPoints[0],listPoints[1],listPoints[2],listPoints[3]) or not isParallel(listPoints[1],listPoints[2],listPoints[3],listPoints[0]):
            raise InvalidFigureError("Invalid rect")
        self.listPoints = listPoints

class Pentagon():
    """класс пятиугольник"""
    listPoints = []
    def __init__(self, listPoints):
        if not isinstance(listPoints, list):
            raise TypeError("listPoints should have list type")
        if len(listPoints) != 5:
            raise TypeError("listPoints should have 5 elements")
        pointsSet = set()
        for e in listPoints:
            if not isinstance(e,Point):
                raise TypeError("Points should have Point type")
            pointsSet.add((e.x,e.y))
        if len(pointsSet) != 5:
            raise InvalidFigureError("Invalid pentagon")
        for i in range(len(listPoints)):
            for j in range(i+1,len(listPoints)):
                for k in range(j+1,len(listPoints)):
                    if isOnOneLine(listPoints[i],listPoints[j],listPoints[k]):
                        raise InvalidFigureError("Invalid pentagon")
        self.listPoints = listPoints

def is_intersect(rect, pent):
    """проверяет, пересекаются ли прямоугольник и пятиугольник"""
    if not isinstance(rect, Rectangle) or not isinstance(pent,Pentagon):
        raise TypeError("Parameters should have Rectangle and Pentagon types")
    for i in range(len(rect.listPoints)):
        for j in range(i+1,len(rect.listPoints)):
            rectPoint1 = rect.listPoints[i]
            rectPoint2 = rect.listPoints[j]
            A1 = (rectPoint2.y - rectPoint1.y)
            B1 = (rectPoint1.x - rectPoint2.x)
            C1 = rectPoint1.y*(rectPoint2.x - rectPoint1.x) - rectPoint1.x*(rectPoint2.y - rectPoint1.y)
            for k in range(len(pent.listPoints)):
                for l in range(k+1,len(pent.listPoints)):
                    pentPoint1 = pent.listPoints[k]
                    pentPoint2 = pent.listPoints[l]
                    A2 = (pentPoint2.y - pentPoint1.y)
                    B2 = (pentPoint1.x - pentPoint2.x)
                    C2 = pentPoint1.y*(pentPoint2.x - pentPoint1.x) - pentPoint1.x*(pentPoint2.y - pentPoint1.y)
                    if (A1*B2-A2*B1) == 0:
                        continue
                    xIntersect = -(C1*B2-C2*B1)/(A1*B2-A2*B1)
                    yIntersect = -(A1*C2-A2*C1)/(A1*B2-A2*B1)
                    if xIntersect >= max(min(rectPoint1.x,rectPoint2.x),min(pentPoint1.x,pentPoint2.x)) and xIntersect <= min(max(rectPoint1.x,rectPoint2.x),max(pentPoint1.x,pentPoint2.x)):
                        if yIntersect >= max(min(rectPoint1.y,rectPoint2.y),min(pentPoint1.y,pentPoint2.y)) and yIntersect <= min(max(rectPoint1.y,rectPoint2.y),max(pentPoint1.y,pentPoint2.y)):
                            return True         
    return False

def is_include(rect, pent):
    """проверяет факт включения пятиугольника в прямоугольник"""
    if not isinstance(rect, Rectangle) or not isinstance(pent,Pentagon):
        raise TypeError("Parameters should have Rectangle and Pentagon types")
    A,B,C = [],[],[]
    for i in range(len(rect.listPoints)-1):
        j = i + 1
        rectPoint1 = rect.listPoints[i]
        rectPoint2 = rect.listPoints[j]
        A.append(rectPoint2.y - rectPoint1.y)
        B.append(rectPoint1.x - rectPoint2.x)
        C.append(rectPoint1.y*(rectPoint2.x - rectPoint1.x) - rectPoint1.x*(rectPoint2.y - rectPoint1.y))
    rectPoint1 = rect.listPoints[3]
    rectPoint2 = rect.listPoints[0]
    A.append(rectPoint2.y - rectPoint1.y)
    B.append(rectPoint1.x - rectPoint2.x)
    C.append(rectPoint1.y*(rectPoint2.x - rectPoint1.x) - rectPoint1.x*(rectPoint2.y - rectPoint1.y))
    for pentPoint in pent.listPoints:
        xIntersect = []
        yIntersect = []
        for i in range(4):
            xIntersect.append((-A[i]*C[i]+B[i]*(B[i]*pentPoint.x-A[i]*pentPoint.y))/(A[i]**2+B[i]**2))
            yIntersect.append(-(A[i]*(B[i]*pentPoint.x-A[i]*pentPoint.y)+B[i]*C[i])/(A[i]**2+B[i]**2))
        if ((xIntersect[0]-pentPoint.x)*(xIntersect[2]-pentPoint.x) + (yIntersect[0]-pentPoint.y)*(yIntersect[2]-pentPoint.y))/((xIntersect[0]-pentPoint.x)*(xIntersect[0]-pentPoint.x) + (yIntersect[0]-pentPoint.y)*(yIntersect[0]-pentPoint.y))**(0.5)/((xIntersect[2]-pentPoint.x)*(xIntersect[2]-pentPoint.x) + (yIntersect[2]-pentPoint.y)*(yIntersect[2]-pentPoint.y))**(0.5) != -1:
            return False
        if ((xIntersect[1]-pentPoint.x)*(xIntersect[3]-pentPoint.x) + (yIntersect[1]-pentPoint.y)*(yIntersect[3]-pentPoint.y))/((xIntersect[1]-pentPoint.x)*(xIntersect[1]-pentPoint.x) + (yIntersect[1]-pentPoint.y)*(yIntersect[1]-pentPoint.y))**(0.5)/((xIntersect[3]-pentPoint.x)*(xIntersect[3]-pentPoint.x) + (yIntersect[3]-pentPoint.y)*(yIntersect[3]-pentPoint.y))**(0.5) != -1:
            return False
    return True


try:
    #rect = Rectangle([Point(0,0),Point(0,1),Point(1,1),Point(1,0)])
    #pent = Pentagon([Point(0.5,0.5),Point(0.5,1.5),Point(1.5,1.5),Point(2,1),Point(1.5,0.5)])
    rect = Rectangle([Point(0,0),Point(0,1),Point(1,1),Point(1,0)])
    pent = Pentagon([Point(0.25,0.25),Point(0.25,0.75),Point(0.75,0.75),Point(0.9,0.5),Point(0.75,0.25)])
    print(is_intersect(rect,pent))
    print(is_include(rect,pent))
except (TypeError, InvalidFigureError) as e:
    print(e)