import numpy as np
import random
from operator import itemgetter
import copy
from matplotlib import pyplot as plt 


class evolutionaryAlgorithmClass():

    def __init__(self,numberOfCourses,numberOfProfessors,numberOfLectureHalls,
                totalNumberDays,totalHours,numberOfChromosomes,topK):
    
        self.numberOfCourses=numberOfCourses
        self.numberOfProfessors=numberOfProfessors
        self.numberOfLectureHalls=numberOfLectureHalls

        self.totalNumberDays=totalNumberDays
        self.totalHours=totalHours

        self.numberOfChromosomes=numberOfChromosomes
        self.topK=topK
        self.courseAndProfList=self.createCourseAndProfList()
        self.totalMutationZaxis=self.numberOfLectureHalls-int(.6*(self.numberOfLectureHalls))
        self.totalMutationXYaxis=self.totalHours-int(.4*(self.totalHours))
        
    def genRandNumber(self,number):
        return random.randint(0,number-1)
    

    def createCourseAndProfList(self):
        courseAndProfList=[]
        profCount=0
        for i in range(self.numberOfCourses):

            currentCourseAndProf=[i,profCount]
            if(profCount>=self.numberOfProfessors-1):
                profCount=0
            else:
                profCount+=1
            courseAndProfList.append(currentCourseAndProf)
            
        
        return courseAndProfList

    def singleChormosomeFunction(self):
        temp=self.courseAndProfList+self.courseAndProfList
        chromosome=np.full((self.totalNumberDays,self.totalHours,self.numberOfLectureHalls,2),-1)
        checkCourseList=[2]*self.numberOfCourses
        uniqueSet=set()

        for currentCourse in temp:

            while(True):
                # print("gfdgdf")
                
                randomDay=self.genRandNumber(self.totalNumberDays)
                randomHour=self.genRandNumber(self.totalHours)
                randomLecture=self.genRandNumber(self.numberOfLectureHalls)
           
                if(tuple([randomDay,randomHour,randomLecture]) not in uniqueSet):
                    uniqueSet.add(tuple([randomDay,randomHour,randomLecture]))
                    break

            chromosome[randomDay,randomHour,randomLecture,:]=np.array(currentCourse)

        return chromosome

    def generateChormosomes(self):

        totalChormosomes=[]
        for i in range(self.numberOfChromosomes):
            currentChomosome=self.singleChormosomeFunction()
            totalChormosomes.append(currentChomosome)
        return np.array(totalChormosomes)

    # FITNESS FUNCTIONS
    def zAxisFitnessFunction(self,chormosome):
        
        collisionLecture=0
        collisionProf=0
                
        for currentDay in range(self.totalNumberDays):
            for currentHour in range(self.totalHours):
                # print("************")
                uniqueLectures=set()
                uniqueProf=set()
                
                
                for currentLecture in range(self.numberOfLectureHalls):
                    currentCourse=chormosome[currentDay,currentHour,currentLecture,0]
                    currentProf=chormosome[currentDay,currentHour,currentLecture,1]
                    if(currentCourse>=0):
                        if(currentCourse not in uniqueLectures):
                            uniqueLectures.add(currentCourse)
                        else:
                            collisionLecture+=1
                    
                    if(currentProf>=0):
                        if(currentProf not in uniqueProf):
                            uniqueProf.add(currentProf)
                        else:
                            collisionProf+=1

        return collisionLecture+collisionProf

    def twoLecturesPerWeek(self,chormosome):
        totalCoursesList=[0]*self.numberOfCourses
        chormosome=np.array(copy.deepcopy(chormosome))
        for currentDay in range(self.totalNumberDays):
            for currentHour in range(self.totalHours):
                for currentLectureHall in range(self.numberOfLectureHalls):
                    
                    chormosome=chormosome.astype(int)
                    
                    currentCourse=chormosome[currentDay,currentHour,currentLectureHall,0]
                    if(currentCourse>=0):
                        totalCoursesList[currentCourse]+=1
        return totalCoursesList


    def sameLectureSameDayFitness(self,chormosome):

        sameLectureVal=0
        sameProfVal=0

        for currentDay in range(self.totalNumberDays):
            singleDayChromosome=chormosome[currentDay,:,:,:]
            # print(singleDayChromosome.shape)

            uniqueLecture=set()
            uniqueProf=set()
        
            # print("**************************")
            for currentDay in singleDayChromosome:
                # print("+++++++++++++++++++++++++")
                for currentLecturHour in currentDay:
                    # print(currentLecturHour)
                    currentLecture=currentLecturHour[0]
                    currentProf=currentLecturHour[1]

                    if(currentLecture>=0):
                        if(currentLecture not in uniqueLecture):
                            uniqueLecture.add(currentLecture)
                        else:
                            sameLectureVal+=1
                    
                    if(currentProf>=0):
                        if(currentProf not in uniqueProf):
                            uniqueProf.add(currentProf)
                        else:
                            sameProfVal+=1

                # print(sameLectureVal)
                # print(sameProfVal)   
                    

        return sameLectureVal+sameProfVal


    def twoLecturesPenalityFunction(self,chromosome):
        twoLecturePenality=0
        for i in self.twoLecturesPerWeek(chromosome):
            if(i>3):
                twoLecturePenality+=1

        return twoLecturePenality

    def totalTwoLecturesPenalityFunction(self,totalChomosomes):
        totalTwoLecturesPenalityValues=[]
        for currentChomosome in totalChomosomes:
            fitnessValue=self.twoLecturesPenalityFunction(currentChomosome)

            totalTwoLecturesPenalityValues.append(fitnessValue)
        return np.array(totalTwoLecturesPenalityValues)
   
    def singleCollisionFunction(self,chormosome):

        fitnessZAxis=self.zAxisFitnessFunction(chormosome)
    
        sameLectureSameDayFitnessVal=self.sameLectureSameDayFitness(chormosome)
        fitnessValue=fitnessZAxis+sameLectureSameDayFitnessVal
        # twoLecturesPenality=self.twoLecturesPenalityFunction(chormosome)
        return fitnessValue #+ twoLecturesPenality

    def totalFitnessFunction(self,totalChromosomes):
        totalFitnessvalues=[]
        for currentChomosome in totalChromosomes:
                fitnessValue=self.singleCollisionFunction(currentChomosome)
                totalFitnessvalues.append(fitnessValue)
        return np.array(totalFitnessvalues)

    def sortFitnessfunction(self,totalChormosomes,totalFitnessValues):
        
        newFitnessValues=totalFitnessValues.argsort()
        newChromsomes=totalChormosomes[newFitnessValues]
        return newChromsomes

    def selectTopKChromosomes(self,chromosomes):
        return chromosomes[:self.topK,:,:,:,:]

    def zAxisCrossoverFunction(self,chormosome1,chormosome2):

        offSpring1=np.empty((self.totalNumberDays,self.totalHours,self.numberOfLectureHalls,2))
        offSpring2=np.empty((self.totalNumberDays,self.totalHours,self.numberOfLectureHalls,2))

        crossoverPoint=self.genRandNumber(self.numberOfLectureHalls)
        # print(crossoverPoint)
        offSpring1[:,:,:crossoverPoint]=chormosome1[:,:,:crossoverPoint]
        offSpring1[:,:,self.numberOfLectureHalls-crossoverPoint:]=chormosome2[:,:,self.numberOfLectureHalls-crossoverPoint:]
        
        offSpring2[:,:,:crossoverPoint]=chormosome2[:,:,:crossoverPoint]
        offSpring2[:,:,self.numberOfLectureHalls-crossoverPoint:]=chormosome1[:,:,self.numberOfLectureHalls-crossoverPoint:]
        
        return (np.array(offSpring1)).astype(int),(np.array(offSpring2)).astype(int)

    def xyAxisCrossOverFunction(self,chormosome1,chormosome2):

        offSpring1=np.empty((self.totalNumberDays,self.totalHours,self.numberOfLectureHalls,2))
        offSpring2=np.empty((self.totalNumberDays,self.totalHours,self.numberOfLectureHalls,2))

        crossoverPoint=self.genRandNumber(self.totalHours)

        offSpring1[:,:crossoverPoint,:]=chormosome1[:,:crossoverPoint,:]
        offSpring1[:,self.numberOfLectureHalls-crossoverPoint:,:]=chormosome2[:,self.numberOfLectureHalls-crossoverPoint:,:]
        
        offSpring2[:,:crossoverPoint,:]=chormosome2[:,:crossoverPoint,:]
        offSpring2[:,self.numberOfLectureHalls-crossoverPoint:,:]=chormosome1[:,self.numberOfLectureHalls-crossoverPoint:,:]
        
        return (np.array(offSpring1)).astype(int),(np.array(offSpring2)).astype(int)


    def singleCrossoverFunction(self,chormosome1,chormosome2):

        totaloffSpring=[]
        zAxisOffSpring=self.zAxisCrossoverFunction(chormosome1,chormosome2)
        xyAxisOffSpring=self.xyAxisCrossOverFunction(chormosome1,chormosome2)

        ZaxisXYOffSpring=self.xyAxisCrossOverFunction(zAxisOffSpring[0],zAxisOffSpring[1])
        xyaxisZoffSpring=self.zAxisCrossoverFunction(xyAxisOffSpring[0],xyAxisOffSpring[1])


        totaloffSpring.append(zAxisOffSpring[0])
        totaloffSpring.append(zAxisOffSpring[1])
        
        totaloffSpring.append(xyAxisOffSpring[0])
        totaloffSpring.append(xyAxisOffSpring[1])
        
        totaloffSpring.append(ZaxisXYOffSpring[0])
        totaloffSpring.append(ZaxisXYOffSpring[1])
        

        totaloffSpring.append(xyaxisZoffSpring[0])
        totaloffSpring.append(xyaxisZoffSpring[1])
        
        return totaloffSpring

    def totalCrossOver(self,chromosomes):
        newOffSprings=[]

        for i in range(len(chromosomes)):
            for j in range(len(chromosomes)):
                newOffSpring=self.singleCrossoverFunction(chromosomes[i],chromosomes[j])
    
                for i in range(len(newOffSpring)):
                    newOffSprings.append(newOffSpring[i])
        
        return np.array(newOffSprings)

    def createNewGeneration(self,sortedChromosomes,newOffSprings):
        
        newGeneration=np.concatenate((sortedChromosomes,newOffSprings))
        fitnessValueNewGen=self.totalFitnessFunction(newGeneration)
        sortedNewGeneration=self.sortFitnessfunction(newGeneration,fitnessValueNewGen)
        return sortedNewGeneration

    def zAxisSingleMutationFunction(self,chormosome):
        for currentMutation in range(self.totalMutationZaxis):
            pointOfMutationDay=self.genRandNumber(self.totalNumberDays)
            pointOfMutationHour=self.genRandNumber(self.totalHours)
            
            randomChormosome=self.singleChormosomeFunction()
                
            chormosome[pointOfMutationDay,pointOfMutationHour,:,:]=randomChormosome[pointOfMutationDay,pointOfMutationHour,:,:]  
        return chormosome

    def xyAxisSingleMutationFunction(self,chormosome):
        # print(self.totalMutationXYaxis)
        newChormosome=copy.deepcopy(chormosome)

        for currentMutation in range(self.totalMutationXYaxis):
            
            pointOfMutation=self.genRandNumber(self.totalNumberDays)
            # print(pointOfMutation)
            # print(newChormosome[0,:,:,:].shape)
            randomChormosome=self.singleChormosomeFunction()
            # print(randomChormosome[pointOfMutation,:,:,:])
            newChormosome[pointOfMutation,:,:,:]=copy.deepcopy(randomChormosome[pointOfMutation,:,:,:])  

        return newChormosome

    
    def singleMutationFunction(self,chormosome):

        chormosomeZaxis=self.zAxisSingleMutationFunction(chormosome)
        chormosomeXYaxis=self.xyAxisSingleMutationFunction(chormosome)
  
        return chormosomeZaxis,chormosomeXYaxis

    def totalMutationFunction(self,totalChormosomes):
        newMutationGeneration=[]
        tempGeneration=copy.deepcopy(totalChormosomes)
        
        for currentChomosome in tempGeneration:
            mututatedGenration=self.singleMutationFunction(currentChomosome)

            newMutationGeneration.append(mututatedGenration[0])
            newMutationGeneration.append(mututatedGenration[1])
        return np.array(newMutationGeneration)

    def swapZAxis(self,chormosome,currentDayIndex,currentHourIndex,currentLectureIndex):

        newChormosome=copy.deepcopy(chormosome)
        currentLecture=newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]         
        if(currentLectureIndex==0):
            # print("SWAPING IN FORWARD DIRECTION ONLY")
            count=1
            while(count!=2):
                # print("I: "+str(count))                
                tempCourse=newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex+count,:]
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex+count,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempCourse
                
                newChormosomeVal=self.zAxisFitnessFunction(newChormosome)
                originalChormosomeVal=self.zAxisFitnessFunction(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                else:
                    # print("NO SWAPING")
                    newChormosome=copy.deepcopy(chormosome)
                count+=1    

        elif(currentLectureIndex==self.numberOfLectureHalls-1):
            # print("SWAPING IN BACKWARD DIRECTION ONLY")

            count=1
            while(count!=2):
                # print("I: "+str(count))                
                tempCourse=newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex-count,:]
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex-count,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempCourse
                
                newChormosomeVal=self.zAxisFitnessFunction(newChormosome)
                originalChormosomeVal=self.zAxisFitnessFunction(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                
                else:
                    # print("NO SWAPING")
                    newChormosome=copy.deepcopy(chormosome)
                    
                count+=1    
        else:
            # print("swap in both direction")

            count=1
            while(count!=2):
                # print("I: "+str(count))  

                tempForwardCourse=newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex+count,:]
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex+count,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempForwardCourse
            
                newChormosomeVal=self.zAxisFitnessFunction(newChormosome)
                originalChormosomeVal=self.zAxisFitnessFunction(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                else:
                    # print("NO SWAPING")
                    newChormosome=copy.deepcopy(chormosome)
                    

                    
                tempBackwardCourse=newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex-count,:]
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex-count,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempBackwardCourse
                newChormosomeVal=self.zAxisFitnessFunction(newChormosome)
                originalChormosomeVal=self.zAxisFitnessFunction(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break

                else:
                    # print("NO SWAPING")
                    newChormosome=copy.deepcopy(chormosome)
                        
                count+=1 

        return chormosome 
                
    def zAxisLocalSearch(self,chormosome):
        
        for currentDayIndex in range(self.totalNumberDays):
            # print("++++++++++++++++")
            for currentHourIndex in range(self.totalHours):
                # print("************")
                uniqueLectures=set()
                uniqueProf=set()
                # print(currentDayIndex)
                for currentLectureIndex in range(self.numberOfLectureHalls):

                    currentLecture=chormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]
                    currentCourse=chormosome[currentDayIndex,currentHourIndex,currentLectureIndex,0]
                    currentProf=chormosome[currentDayIndex,currentHourIndex,currentLectureIndex,1]
                    # print(chormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:])
                    # print("Current Day:"+str(currentDayIndex))
                    # print("Current hour: "+str(currentHourIndex))
                    # print("Current Lecture Index: "+str(currentLectureIndex))
                    # print("ORIGINAL FITNESS VALUES: "+str(self.zAxisFitnessFunction(chormosome)))

                    if(currentCourse>=0):
                        if(currentCourse not in uniqueLectures):
                            uniqueLectures.add(currentCourse)
                        else:
                            # print("COLLISION IN LECTURES")
                            chormosome=self.swapZAxis(chormosome,currentDayIndex,currentHourIndex,currentLectureIndex)
  
                    if(currentProf>=0):
                        if(currentProf not in uniqueProf):
                            uniqueProf.add(currentProf)
                        else:
                            # print("COLLSION IN PROFESSORS")
                            chormosome=self.swapZAxis(chormosome,currentDayIndex,currentHourIndex,currentLectureIndex)


        return chormosome                  

    def swapXYAxis(self,chormosome,currentDayIndex,currentHourIndex,currentLectureIndex):
        # print("ORIGINAL FITNESS VALUES: "+str(self.sameLectureSameDayFitness(chormosome)))
        
        currentLecture=chormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]          
        newChormosome=copy.deepcopy(chormosome)

        if(currentDayIndex==0):
            # print("SWAPING IN FORWARD DIRECTION ONLY")
            count=1
            while(count!=2):
                # print("I: "+str(count))                
                tempCourse=newChormosome[currentDayIndex+count,currentHourIndex,currentLectureIndex,:]
                newChormosome[currentDayIndex+count,currentHourIndex,currentLectureIndex,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempCourse
                
                newChormosomeVal=self.sameLectureSameDayFitness(newChormosome)
                originalChormosomeVal=self.sameLectureSameDayFitness(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)

                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break

                else:

                    newChormosome=copy.deepcopy(chormosome)
                count+=1    

        elif(currentDayIndex==self.totalNumberDays-1):
            # print("SWAPING IN BACKWARD DIRECTION ONLY")

            count=1
            while(count!=2):
                # print("I: "+str(count))                
                tempCourse=newChormosome[currentDayIndex-count,currentHourIndex,currentLectureIndex,:]
                newChormosome[currentDayIndex-count,currentHourIndex,currentLectureIndex-count,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempCourse
                
                newChormosomeVal=self.sameLectureSameDayFitness(newChormosome)
                originalChormosomeVal=self.sameLectureSameDayFitness(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                
                else:
                    newChormosome=copy.deepcopy(chormosome)
                count+=1    
        else:
            # print("swap in both direction")

            count=1
            while(count!=2):
                # print("I: "+str(count))  

                tempForwardCourse=newChormosome[currentDayIndex+count,currentHourIndex,currentLectureIndex,:]
                newChormosome[currentDayIndex+count,currentHourIndex,currentLectureIndex,:]=currentLecture
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=tempForwardCourse
            
                newChormosomeVal=self.sameLectureSameDayFitness(newChormosome)
                originalChormosomeVal=self.sameLectureSameDayFitness(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
                
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                else:
                    newChormosome=copy.deepcopy(chormosome)
                    

                
                tempBackwardCourse=newChormosome[currentDayIndex-count,currentHourIndex,currentLectureIndex,:]
                newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:]=currentLecture
                newChormosome[currentDayIndex-count,currentHourIndex,currentLectureIndex,:]=tempBackwardCourse
                originalChormosomeVal=self.sameLectureSameDayFitness(chormosome)
                # print(newChormosomeVal)
                # print(originalChormosomeVal)
            
                if(originalChormosomeVal>newChormosomeVal):
                    # print("*******************CHROMOSOME UPDATED********************")
                    chormosome=newChormosome
                    break
                
                else:
                    newChormosome=copy.deepcopy(chormosome)
            
                count+=1 

        return chormosome 


    
    def XYAxisLocalSearch(self,chormosome):  
        for currentDayIndex in range(self.totalNumberDays):
        
            singleDayChromosome=chormosome[currentDayIndex,:,:,:]
            # print(singleDayChromosome.shape)

            uniqueLecture=set()
            uniqueProf=set()
            # print("**************************")
            for currentHourIndex in range(self.totalHours):
                # print("//////////////////////////////////")
                for currentLectureHallIndex in range(self.numberOfLectureHalls):
                    # print(newChormosome[currentDayIndex,currentHourIndex,currentLectureIndex,:])
                    # print("Current Day:"+str(currentDayIndex))
                    # print("Current hour: "+str(currentHourIndex))
                    # print("Current Lecture Index: "+str(currentLectureHallIndex))
                    # print("ORIGINAL FITNESS VALUES: "+str(self.sameLectureSameDayFitness(chormosome)))

                    
                    currentLectureHall=chormosome[currentDayIndex,currentHourIndex,currentLectureHallIndex,:]
                    # print("+++++++++++++++++++++++++")

                    currentLecture=currentLectureHall[0]
                    currentProf=currentLectureHall[1]

                    if(currentLecture>=0):
                        if(currentLecture not in uniqueLecture):
                            uniqueLecture.add(currentLecture)
                        else:
                            # print("COLLISION IN LECTURES")
                            chormosome=self.swapXYAxis(chormosome,currentDayIndex,currentHourIndex,currentLectureHallIndex)
                    if(currentProf>=0):
                        if(currentProf not in uniqueProf):
                            uniqueProf.add(currentProf)
                        else:
                            # print("COLLISION IN PROFS")
                            chormosome=self.swapXYAxis(chormosome,currentDayIndex,currentHourIndex,currentLectureHallIndex)

        return chormosome

    

    def localSearch(self,chormosome):
        zAxisNewchormosome=self.zAxisLocalSearch(chormosome)

        return np.array(self.XYAxisLocalSearch(zAxisNewchormosome)) 

    def totalLocalSearch(self,totalChomosomes):

        newGeneration=[]
        for currentChormosome in totalChomosomes:
            newGeneration.append(self.localSearch(currentChormosome))
            
        return np.array(newGeneration)





   
    def geneticFit(self):
        print("*"*20+"GENETIC ALGORITHM"+"*"*20)
        totalChomosomes=self.generateChormosomes()
        terminateFlag=True
        count=0
        totalFitnessValForPlot=[]
        while(terminateFlag):

            print("*"*20+str(count)+"*"*20)
            count+=1
            totalFitnessVal=self.totalFitnessFunction(totalChomosomes)
            print("FINDING....")
        
            sortedChromosomes=self.sortFitnessfunction(totalChomosomes,totalFitnessVal)
            print("TOP PERFORMING CHROMOSOME: "+str(self.singleCollisionFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME Z FITNESS: "+str(self.zAxisFitnessFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME XY FITNESS: "+str(self.sameLectureSameDayFitness(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME SAME LECTURE FITNESS: "+str(self.twoLecturesPenalityFunction(sortedChromosomes[0])))
            
            
            totalFitnessValForPlot.append(self.singleCollisionFunction(sortedChromosomes[0]))
            if(self.singleCollisionFunction(sortedChromosomes[0])==0 or count==20):
                print("**************CONVERGE****************")
                result=sortedChromosomes.astype(int)
                print(result)    
                terminateFlag=False
                plt.plot(range(count),totalFitnessValForPlot)
                plt.title("FITNESS VS NUMBER OF ITERATIONS")
                plt.xlabel("NUMBER OF ITERATIONS")
                plt.ylabel("FITNESS VALUE")

                plt.show()

                print("NOW TWO LECTURES PER WEEK FITNESS CRITERIA IS CHECKING")
                totalTwoLecturePenalityValues=self.totalTwoLecturesPenalityFunction(sortedChromosomes)
                print(totalTwoLecturePenalityValues)
                sortedTwoLecturesPenalityChromosomes=self.sortFitnessfunction(sortedChromosomes,totalTwoLecturePenalityValues)
                print(self.twoLecturesPerWeek(sortedTwoLecturesPenalityChromosomes[0]))
                print(sortedTwoLecturesPenalityChromosomes[0])
                break
            else:
                topKChromosomes=self.selectTopKChromosomes(sortedChromosomes)
        
                offSprings=self.totalCrossOver(topKChromosomes)

                newGeneration=self.createNewGeneration(sortedChromosomes,offSprings)
            
                crossoverPopulation=newGeneration[:self.numberOfChromosomes,:,:,:]
                print("TOP PERFORMING CHROMOSOME AFTER CROSSOVER: "+str(self.singleCollisionFunction(crossoverPopulation[0])))
                print(self.totalFitnessFunction(crossoverPopulation))
            
                mutatedGeneration=self.totalMutationFunction(crossoverPopulation)
            
                mutationPopulation=self.createNewGeneration(crossoverPopulation,mutatedGeneration)
                
                populationAftermutation=mutationPopulation[:self.numberOfChromosomes,:,:,:]

                print(self.totalFitnessFunction(populationAftermutation))
            
            
                print("TOP PERFORMING CHROMOSOME AFTER MUTATION: "+str(self.singleCollisionFunction(populationAftermutation[0])))
                totalChomosomes=populationAftermutation
                # totalChomosomes=crossoverPopulation


    def memeticFit(self):
        print("*"*20+"MEMETIC ALGORITHM"+"*"*20)
        totalChomosomes=self.generateChormosomes()
        totalNewChomosomes=self.totalLocalSearch(totalChomosomes)
        terminateFlag=True
        count=0
        totalFitnessValForPlot=[]
        while(terminateFlag):

            print("*"*20+str(count)+"*"*20)
            count+=1
            totalFitnessVal=self.totalFitnessFunction(totalNewChomosomes)
            print("FINDING....")
        
            sortedChromosomes=self.sortFitnessfunction(totalNewChomosomes,totalFitnessVal)
            print("TOP PERFORMING CHROMOSOME: "+str(self.singleCollisionFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME Z FITNESS: "+str(self.zAxisFitnessFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME XY FITNESS: "+str(self.sameLectureSameDayFitness(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME SAME LECTURE FITNESS: "+str(self.twoLecturesPenalityFunction(sortedChromosomes[0])))
            
            
            totalFitnessValForPlot.append(self.singleCollisionFunction(sortedChromosomes[0]))
            if(self.singleCollisionFunction(sortedChromosomes[0])==0 or count==20):
                print("**************CONVERGE****************")
                result=sortedChromosomes.astype(int)
                print(result)    
                terminateFlag=False
                plt.plot(range(count),totalFitnessValForPlot)
                plt.title("FITNESS VS NUMBER OF ITERATIONS-MEMTIC")
                plt.xlabel("NUMBER OF ITERATIONS")
                plt.ylabel("FITNESS VALUE")
                plt.show()

                print("NOW TWO LECTURES PER WEEK FITNESS CRITERIA IS CHECKING")
                totalTwoLecturePenalityValues=self.totalTwoLecturesPenalityFunction(sortedChromosomes)
                print(totalTwoLecturePenalityValues)
                sortedTwoLecturesPenalityChromosomes=self.sortFitnessfunction(sortedChromosomes,totalTwoLecturePenalityValues)
                print(self.twoLecturesPerWeek(sortedTwoLecturesPenalityChromosomes[0]))
                print(sortedTwoLecturesPenalityChromosomes[0])
                break
            else:
                topKChromosomes=self.selectTopKChromosomes(sortedChromosomes)
        
                offSprings=self.totalCrossOver(topKChromosomes)

                newGeneration=self.createNewGeneration(sortedChromosomes,offSprings)
            
                crossoverPopulation=newGeneration[:self.numberOfChromosomes,:,:,:]
                print("TOP PERFORMING CHROMOSOME AFTER CROSSOVER: "+str(self.singleCollisionFunction(crossoverPopulation[0])))
            
            
                mutatedGeneration=self.totalMutationFunction(crossoverPopulation)
            
                mutationPopulation=self.createNewGeneration(crossoverPopulation,mutatedGeneration)
                
                populationAftermutation=mutationPopulation[:self.numberOfChromosomes,:,:,:]
            
            
                populationAfterLocalSearch=self.totalLocalSearch(populationAftermutation)
                print("TOP PERFORMING CHROMOSOME AFTER MUTATION: "+str(self.singleCollisionFunction(populationAfterLocalSearch[0])))
                totalNewChomosomes=populationAfterLocalSearch
                # totalChomosomes=crossoverPopulation


    def compare(self):
        print("*"*20+"GENETIC ALGORITHM"+"*"*20)
        totalRawChomosomes=self.generateChormosomes()
        totalChomosomes=totalRawChomosomes
        terminateFlag=True

        countGenetic=0
        countMemtic=0      
        totalFitnessValForPlotGenetic=[]
        totalFitnessValForPlotMemetic=[]
        
        while(terminateFlag):

            print("*"*20+str(countGenetic)+"*"*20)
            countGenetic+=1
            totalFitnessVal=self.totalFitnessFunction(totalChomosomes)
            print("FINDING....")
        
            sortedChromosomes=self.sortFitnessfunction(totalChomosomes,totalFitnessVal)
            print("TOP PERFORMING CHROMOSOME: "+str(self.singleCollisionFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME Z FITNESS: "+str(self.zAxisFitnessFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME XY FITNESS: "+str(self.sameLectureSameDayFitness(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME SAME LECTURE FITNESS: "+str(self.twoLecturesPenalityFunction(sortedChromosomes[0])))
            
            
            totalFitnessValForPlotGenetic.append(self.singleCollisionFunction(sortedChromosomes[0]))
            if(self.singleCollisionFunction(sortedChromosomes[0])==0 or countGenetic==20):
                print("**************CONVERGE****************")
                result=sortedChromosomes.astype(int)
                print(result)    
                terminateFlag=False
                print("NOW TWO LECTURES PER WEEK FITNESS CRITERIA IS CHECKING")
                totalTwoLecturePenalityValues=self.totalTwoLecturesPenalityFunction(sortedChromosomes)
                print(totalTwoLecturePenalityValues)
                sortedTwoLecturesPenalityChromosomes=self.sortFitnessfunction(sortedChromosomes,totalTwoLecturePenalityValues)
                print(self.twoLecturesPerWeek(sortedTwoLecturesPenalityChromosomes[0]))
                print(sortedTwoLecturesPenalityChromosomes[0])
                break
            else:
                topKChromosomes=self.selectTopKChromosomes(sortedChromosomes)
        
                offSprings=self.totalCrossOver(topKChromosomes)

                newGeneration=self.createNewGeneration(sortedChromosomes,offSprings)
            
                crossoverPopulation=newGeneration[:self.numberOfChromosomes,:,:,:]
                print("TOP PERFORMING CHROMOSOME AFTER CROSSOVER: "+str(self.singleCollisionFunction(crossoverPopulation[0])))
                print(self.totalFitnessFunction(crossoverPopulation))
            
                mutatedGeneration=self.totalMutationFunction(crossoverPopulation)
            
                mutationPopulation=self.createNewGeneration(crossoverPopulation,mutatedGeneration)
                
                populationAftermutation=mutationPopulation[:self.numberOfChromosomes,:,:,:]

                print(self.totalFitnessFunction(populationAftermutation))
            
            
                print("TOP PERFORMING CHROMOSOME AFTER MUTATION: "+str(self.singleCollisionFunction(populationAftermutation[0])))
                totalChomosomes=populationAftermutation
                # totalChomosomes=crossoverPopulation

        #///////////////////////////////////////////////////////////////////////////////////////////////////////////                # 
        print("*"*20+"MEMETIC ALGORITHM"+"*"*20)
        totalChomosomes=totalRawChomosomes
        totalNewChomosomes=self.totalLocalSearch(totalChomosomes)
        terminateFlag=True
        while(terminateFlag):

            print("*"*20+str(countMemtic)+"*"*20)
            countMemtic+=1
            totalFitnessVal=self.totalFitnessFunction(totalNewChomosomes)
            print("FINDING....")
        
            sortedChromosomes=self.sortFitnessfunction(totalNewChomosomes,totalFitnessVal)
            print("TOP PERFORMING CHROMOSOME: "+str(self.singleCollisionFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME Z FITNESS: "+str(self.zAxisFitnessFunction(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME XY FITNESS: "+str(self.sameLectureSameDayFitness(sortedChromosomes[0])))
            print("TOP PERFORMING CHROMOSOME SAME LECTURE FITNESS: "+str(self.twoLecturesPenalityFunction(sortedChromosomes[0])))
            
            
            totalFitnessValForPlotMemetic.append(self.singleCollisionFunction(sortedChromosomes[0]))
            if(self.singleCollisionFunction(sortedChromosomes[0])==0 or countMemtic==20):
                print("**************CONVERGE****************")
                result=sortedChromosomes.astype(int)
                print(result)    
                terminateFlag=False
                plt.plot(range(countMemtic),totalFitnessValForPlotGenetic)
                plt.plot(range(countGenetic),totalFitnessValForPlotMemetic)
                plt.legend(["GA","MA"],loc="upper left")

                plt.title("FITNESS VS NUMBER OF ITERATIONS")
                plt.xlabel("NUMBER OF ITERATIONS")
                plt.ylabel("FITNESS VALUE")
                plt.show()

                print("NOW TWO LECTURES PER WEEK FITNESS CRITERIA IS CHECKING")
                totalTwoLecturePenalityValues=self.totalTwoLecturesPenalityFunction(sortedChromosomes)
                print(totalTwoLecturePenalityValues)
                sortedTwoLecturesPenalityChromosomes=self.sortFitnessfunction(sortedChromosomes,totalTwoLecturePenalityValues)
                print(self.twoLecturesPerWeek(sortedTwoLecturesPenalityChromosomes[0]))
                print(sortedTwoLecturesPenalityChromosomes[0])
                break
            else:
                topKChromosomes=self.selectTopKChromosomes(sortedChromosomes)
        
                offSprings=self.totalCrossOver(topKChromosomes)

                newGeneration=self.createNewGeneration(sortedChromosomes,offSprings)
            
                crossoverPopulation=newGeneration[:self.numberOfChromosomes,:,:,:]
                print("TOP PERFORMING CHROMOSOME AFTER CROSSOVER: "+str(self.singleCollisionFunction(crossoverPopulation[0])))
            
            
                mutatedGeneration=self.totalMutationFunction(crossoverPopulation)
            
                mutationPopulation=self.createNewGeneration(crossoverPopulation,mutatedGeneration)
                
                populationAftermutation=mutationPopulation[:self.numberOfChromosomes,:,:,:]
            
            
                populationAfterLocalSearch=self.totalLocalSearch(populationAftermutation)
                print("TOP PERFORMING CHROMOSOME AFTER MUTATION: "+str(self.singleCollisionFunction(populationAfterLocalSearch[0])))
                totalNewChomosomes=populationAfterLocalSearch
                # totalChomosomes=crossoverPopulation
                
