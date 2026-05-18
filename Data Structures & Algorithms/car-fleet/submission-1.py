class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # pairs = [[7,1], [4,2], [1,2], [0,1]]
        # stack = [3, 4.5, 10]
        # times = [10, 4.5, 3, 3]

        fleet = []
        pairs = []
        # pair up positions and speeds
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        # sort them in desc order
        pairs.sort(reverse=True)

        # loop through pairs
        # for each pair, calculate its time to target
        for p,s in pairs:
            time = (target - p)/s

            # if stack and curr time > last thing in stack
            if fleet and time <= fleet[-1]:
                continue
            fleet.append(time)

        return len(fleet)
        
            
            
            
            
      

        
       
