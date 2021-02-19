
class CumulativeSumList(object):

    def __init__(self, list_no, use_mod=False) -> None:
        mod = int(1e9 + 7)
        if use_mod:
            self._cum_sum_list = self.get_cumulative_sum_list_mod(list_no, mod)
        else:
            self._cum_sum_list = self.get_cumulative_sum_list(list_no)

    def get_sum(self, start, stop):
        """
        元の配列 L_A の A_start + ... + A_{stop-1} を求める
        """
        return self.get_sum_from_cum_sum_list(self._cum_sum_list, start, stop)

    @property
    def cum_sum_list(self):
        return self._cum_sum_list

    @staticmethod
    def get_cumulative_sum_list(list_no):
        """forで累積和を求める。 MOD 使用
        This method works.
        """
        result = [0]
        for number in list_no:
            result.append(result[-1] + number)
        return result

    @staticmethod
    def get_cumulative_sum_list_mod(list_no, mod):
        """forで累積和を求める。 MOD 使用
        This method works.
        """
        result = [0]
        for number in list_no:
            sum = result[-1] + number
            if sum < 0:
                sum += mod
            sum %= mod
            result.append(sum)
        return result

    @staticmethod
    def get_sum_from_cum_sum_list(l_c, start, stop):
        """
        元の配列 L_A の A_start + ... + A_{stop-1} を求める
        """
        return l_c[stop] - l_c[start]
