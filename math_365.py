class Solution(object):

    def get_gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.get_gcd(y, x % y)

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        if y > x:
            x, y = y, x
        if z == 0:
            return True
        else:
            return z % self.get_gcd(x, y) == 0

