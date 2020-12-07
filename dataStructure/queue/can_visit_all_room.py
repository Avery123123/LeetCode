class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue, rooms[0] = rooms[0], False
        while queue:
            k = queue.pop(0)
            if rooms[k]:
                queue.extend(rooms[k])
                rooms[k] = False       
        return not any(rooms)

