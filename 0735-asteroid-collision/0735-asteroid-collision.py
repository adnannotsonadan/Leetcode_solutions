class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[asteroids[0]]
        n=len(asteroids)
        for i in range(1,n):
            while st and asteroids[i]<0 and st[-1]>0 and st[-1]<abs(asteroids[i]) :
                st.pop()
            if st and st[-1]>0 and asteroids[i]<0 :
                if st[-1]==abs(asteroids[i]):
                    st.pop()
                elif st[-1]> abs(asteroids[i]):
                    continue
                elif st[-1]<abs(asteroids[i]):
                    st.append(asteroids[i])
            else:
                st.append(asteroids[i])
        return st
