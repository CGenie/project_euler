#!/usr/bin/python2
# #####################################################################
# test.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import unittest

class Test(unittest.TestCase):
    def test0001(self):
        from id_0001 import ss2

        self.assertEqual(ss2(10), 23)

    def test0002(self):
        from id_0002 import fib, fib_iter
        import itertools

        #f = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        f = list(itertools.islice(fib_iter(), 100))[2:]
        for i, v in enumerate(f):
            self.assertEqual(fib(i + 1), v)
    
    def test0003(self):
        from id_0003 import is_prime, prime_factors

        primes = [2, 3, 5, 7, 11, 13, 17]
        for x in primes:
            self.assertEqual(is_prime(x), 1)

        non_primes = [4, 6, 8, 10, 12, 14, 15, 16, 18]
        for x in non_primes:
            self.assertEqual(is_prime(x), 0)

        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(3), [])
        self.assertEqual(prime_factors(4), [2])
        self.assertEqual(prime_factors(5), [])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(10), [2, 5])

        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])
        
    def test0004(self):
        from id_0004 import palindrome

        self.assertEqual(palindrome(2)[1], 9009)

    def test0005(self):
        from id_0005 import evenly_divisible

        self.assertEqual(evenly_divisible(10), 2520)

    def test0006(self):
        from id_0006 import diff

        self.assertEqual(diff(10), 2640)

    def test0007(self):
        from id_0007 import find_nth_prime

        self.assertEqual(find_nth_prime(6), 13)

    def test0010(self):
        from id_0010 import sum_primes_below

        self.assertEqual(sum_primes_below(10), 17)

    def test0012(self):
        from id_0012 import factors, trinum, trinum_factors

        self.assertEqual(set(factors(30)), set([1, 2, 3, 5, 6, 10, 15, 30]))

        self.assertEqual(trinum(7), 28)
        #self.assertEqual(trinum_factors(5), 28)

    def test0013(self):
        from id_0013 import first_n_digits

        self.assertEqual(first_n_digits(123456789, 3), "123")

    def test0014(self):
        from id_0014 import collatz_chain

        self.assertEqual(collatz_chain(13), 10)

    def test0015(self):
        from id_0015 import routes, routes2

        self.assertEqual(routes(0, 0, 2), 6)
        for x in range(2, 10):
            self.assertEqual(routes(0, 0, x), routes2(x))

    def test0016(self):
        from id_0016 import sum_digits

        self.assertEqual(sum_digits(2**15), 26)

    def test0017(self):
        from id_0017 import write_number

        self.assertEqual(write_number(22), 'twentytwo')
        self.assertEqual(write_number(76), 'seventysix')
        self.assertEqual(write_number(99), 'ninetynine')
        self.assertEqual(write_number(100), 'onehundred')
        self.assertEqual(write_number(111), 'onehundredandeleven')
        self.assertEqual(write_number(121), 'onehundredandtwentyone')
        self.assertEqual(write_number(342), 'threehundredandfortytwo')
        self.assertEqual(write_number(115), 'onehundredandfifteen')

    def test0018(self):
        from id_0018 import read_triangle, find_maximal_path

        self.assertEqual(read_triangle("10\n11 12\n13 14 15"), [[10], [11, 12], [13, 14, 15]])
        self.assertEqual(find_maximal_path(read_triangle("10\n11 12\n13 14 15")), 37)
        self.assertEqual(find_maximal_path(read_triangle("3\n7 4\n2 4 6\n8 5 9 3")), 23)

    def test0019(self):
        from id_0019 import days_in_month, day_of_week, ymd_increase_by_day

        self.assertEqual(days_in_month(2, year = 1900), 28)
        self.assertEqual(days_in_month(2, year = 1904), 29)
        self.assertEqual(days_in_month(2, year = 1999), 28)
        self.assertEqual(days_in_month(2, year = 2000), 29)

        self.assertEqual(day_of_week(1900, 1, 1), "Monday")
        self.assertEqual(day_of_week(1900, 1, 2), "Tuesday")
        self.assertEqual(day_of_week(1900, 1, 8), "Monday")
        self.assertEqual(day_of_week(1900, 2, 1), "Thursday")
        self.assertEqual(day_of_week(1900, 2, 2), "Friday")
        self.assertEqual(day_of_week(1900, 3, 1), "Thursday")
        self.assertEqual(day_of_week(1900, 4, 1), "Sunday")
        self.assertEqual(day_of_week(1900, 5, 1), "Tuesday")
        self.assertEqual(day_of_week(1900, 6, 1), "Friday")
        self.assertEqual(day_of_week(1900, 7, 1), "Sunday")
        self.assertEqual(day_of_week(1900, 8, 1), "Wednesday")
        self.assertEqual(day_of_week(1900, 9, 1), "Saturday")
        self.assertEqual(day_of_week(1900, 10, 1), "Monday")
        self.assertEqual(day_of_week(1900, 11, 1), "Thursday")
        self.assertEqual(day_of_week(1900, 12, 1), "Saturday")
        self.assertEqual(day_of_week(1900, 12, 2), "Sunday")
        self.assertEqual(day_of_week(1900, 12, 31), "Monday")
        self.assertEqual(day_of_week(2010, 4, 12), "Monday")

        self.assertEqual(ymd_increase_by_day(1900, 1, 1), (1900, 1, 2))
        self.assertEqual(ymd_increase_by_day(1900, 1, 30), (1900, 1, 31))
        self.assertEqual(ymd_increase_by_day(1900, 1, 31), (1900, 2, 1))
        self.assertEqual(ymd_increase_by_day(1900, 2, 28), (1900, 3, 1))
        self.assertEqual(ymd_increase_by_day(1900, 12, 31), (1901, 1, 1))

    def test0021(self):
        from id_0021 import amicable

        self.assertEqual(amicable(220, 284), True)

    def test0022(self):
        from id_0022 import name_alphabetical_value

        self.assertEqual(name_alphabetical_value("COLIN"), 53)

    def test0023(self):
        from id_0023 import is_perfect, is_deficient_prefect_abundant, is_abundant, sum_of_two_abundants

        self.assertEqual(is_perfect(28), True)
        self.assertEqual(is_deficient_prefect_abundant(12), 1)
        self.assertEqual(is_abundant(12), 1)
        self.assertEqual(sum_of_two_abundants(24), True)
        for x in range(2, 24):
            self.assertEqual(sum_of_two_abundants(x), False)

    def test0025(self):
        from id_0025 import fib_n_digits

        self.assertEqual(fib_n_digits(3), 12)

    def test0026(self):
        from id_0026 import has_cycle, cycle_n

        self.assertEqual(has_cycle([1])[0], 0)
        self.assertEqual(has_cycle([1, 2])[0], 0)
        self.assertEqual(has_cycle([1, 2, 1])[0], 0)
        self.assertEqual(has_cycle([1, 2, 1, 2])[0], 2)
        self.assertEqual(has_cycle([1, 2, 1, 3, 1, 3])[0], 2)
        self.assertEqual(cycle_n(2), 0)
        self.assertEqual(cycle_n(4), 0)
        self.assertEqual(cycle_n(6), 1)
        self.assertEqual(cycle_n(7), 6)
        self.assertEqual(cycle_n(51), 16)
        self.assertEqual(cycle_n(486), 27)
        self.assertEqual(cycle_n(999), 3)

    def test0027(self):
        from id_0027 import num_consecutive_primes

        f = lambda n: n**2 + n + 41
        self.assertEqual(num_consecutive_primes(f), 40)
        f = lambda n: n**2 - 79*n + 1601
        self.assertEqual(num_consecutive_primes(f), 80)

    def test0028(self):
        from id_0028 import sum_of_spiral

        self.assertEqual(sum_of_spiral(5), 101)

    def test0029(self):
        from id_0029 import ab_combinations

        self.assertEqual(ab_combinations(5, 5), 15)

    def test0030(self):
        from id_0030 import is_sum_of_nth_powers

        l = [1634, 8208, 9474]
        for n in l:
            self.assertEqual(is_sum_of_nth_powers(n, 4), True)
        for n in range(2, 10000):
            if not n in l:
                self.assertEqual(is_sum_of_nth_powers(n, 4), False)

    def test0031(self):
        from id_0031 import make_value

        self.assertEqual(make_value(1), 1)
        self.assertEqual(make_value(2), 2)
        self.assertEqual(make_value(3), 2)
        self.assertEqual(make_value(4), 3)
        self.assertEqual(make_value(5), 4)

    def test0032(self):
        from id_0032 import is_pandigital

        self.assertEqual(is_pandigital(7254), True)
        self.assertEqual(is_pandigital(1234), False)

    def test0033(self):
        from id_0033 import gcd, is_curious

        self.assertEqual(gcd(15, 10), 5)
        self.assertEqual(gcd(21, 10), 1)
        self.assertEqual(gcd(21, 15), 3)
        self.assertEqual(gcd(8, 3), 1)
        self.assertEqual(gcd(1264, 465), 1)
        self.assertEqual(is_curious((49, 98)), True)

    def test0034(self):
        from id_0034 import is_curious

        self.assertEqual(is_curious(145), True)

    def test0035(self):
        from id_0035 import circulars, is_circular_prime

        self.assertEqual(circulars(197), [197, 971, 719])
        self.assertEqual(is_circular_prime(197), True)

    def test0036(self):
        from id_0036 import is_palindrome, to_base_k

        self.assertEqual(is_palindrome("585"), True)
        self.assertEqual(is_palindrome("586"), False)
        self.assertEqual(is_palindrome("50"), False)
        self.assertEqual(to_base_k(3, 2), "11")
        self.assertEqual(to_base_k(3, 3), "10")
        self.assertEqual(to_base_k(5, 2), "101")
        for x in range(1, 10**3):
            self.assertEqual(str(x), to_base_k(x, 10))
        self.assertEqual(is_palindrome(to_base_k(585, 2)), True)

    def test0037(self):
        from id_0037 import is_truncatable_prime

        self.assertEqual(is_truncatable_prime(3797), True)

    def test0038(self):
        from id_0038 import is_pandigital, pandigital_concatenated_product

        self.assertEqual(is_pandigital(192), False)
        self.assertEqual(is_pandigital(123456789), True)
        self.assertEqual(pandigital_concatenated_product(192)[:2], (True, 3))
        self.assertEqual(pandigital_concatenated_product(9)[:2], (True, 5))

    def test0039(self):
        from id_0039 import num_triangles_with_perimeter

        self.assertEqual(num_triangles_with_perimeter(120), 3)

    def test0040(self):
        from id_0040 import generate_digits

        l = "0123456789101112131415161718192021"
        f = generate_digits()
        for x in l:
            r = f.next()
            self.assertEqual(int(x), r)

    def test0041(self):
        from id_0041 import is_n_pandigital

        self.assertEqual(is_n_pandigital(2143, 4), True)

    def test0042(self):
        from id_0042 import is_triangle_num, is_triangle_word

        for n in range(1, 20):
            self.assertEqual(is_triangle_num(n*(n + 1)/2), True)
        self.assertEqual(is_triangle_word('sky'), True)

    def test0043(self):
        from id_0043 import check_substring_divisibility

        self.assertEqual(check_substring_divisibility(1406357289), True)

    def test0044(self):
        from id_0044 import is_pentagonal

        l = []
        for n in range(2, 20):
            l.append((3*n - 1)*n/2)
        #print l
        for n in xrange(2, l[17] + 1):
            self.assertEqual(is_pentagonal(n), n in l)

    def test0045(self):
        from id_0045 import is_hexagonal

        l = []
        for n in range(2, 30):
            l.append(n*(2*n - 1))
        for x in xrange(2, l[27] + 1):
            self.assertEqual(is_hexagonal(n), n in l)

    def test0046(self):
        from id_0046 import is_goldbachian

        l = [9, 15, 21, 25, 27, 33]
        for n in l:
            self.assertEqual(is_goldbachian(n), True)

    def test0047(self):
        from id_0047 import find_prime_factors, has_k_consecutive_distinct_prime_factors, find_k_consecutive_distinct_prime_factors, count_distinct_factors

        self.assertEqual(find_prime_factors(2), [2])
        self.assertEqual(find_prime_factors(3), [3])
        self.assertEqual(find_prime_factors(4), [2])
        self.assertEqual(find_prime_factors(5), [5])
        self.assertEqual(find_prime_factors(6), [2, 3])
        self.assertEqual(has_k_consecutive_distinct_prime_factors(14, 2), True)
        self.assertEqual(has_k_consecutive_distinct_prime_factors(644, 3), True)
        self.assertEqual(find_k_consecutive_distinct_prime_factors(2), 14)
        self.assertEqual(find_k_consecutive_distinct_prime_factors(3), 644)
        for n in xrange(2, 100):
            self.assertEqual(count_distinct_factors(n), len(find_prime_factors(n)))

    def test0049(self):
        from id_0049 import contains_arithmetic_sequence, is_unusual

        self.assertEqual(contains_arithmetic_sequence([5, 1487, 4817, 8147], 3), True)
        self.assertEqual(is_unusual(1487), True)
        for n in xrange(100, 1000):
            self.assertEqual(is_unusual(n), False)
        for n in xrange(2, 100):
            lst = [10 + n*x for x in xrange(5)]
            for k in xrange(2, 5):
                self.assertEqual(contains_arithmetic_sequence(lst, k), True)

    def test0050(self):
        from id_0050 import sum_consecutive_primes

        self.assertEqual(sum_consecutive_primes(41), 6)
        self.assertEqual(sum_consecutive_primes(953), 21)

    def test0051(self):
        from id_0051 import has_k_primes_generated

        self.assertEqual(has_k_primes_generated(13, 1), 6)
        self.assertEqual(has_k_primes_generated(56003, 2), 7)
        #self.assertEqual(has_k_primes_generated(120383, 3), 8)

    def test0053(self):
        from id_0053 import comb_num
        from itertools import combinations

        for n in range(1, 20):
            for k in range(n):
                cnt = 0
                for c in combinations(range(n), k):
                    cnt += 1
                self.assertEqual(cnt, comb_num(n, k))

    def test0054(self):
        from id_0054 import parse_hand, high_card, one_pair, two_pairs, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, decide_winner
        
        hand1 = [('5', 'D'), ('8', 'C'), ('9', 'S'), ('J', 'S'), ('A', 'C')]
        hand2 = [('2', 'C'), ('5', 'C'), ('7', 'D'), ('8', 'S'), ('Q', 'H')]
        self.assertEqual(high_card(hand1, hand2), 1)
        self.assertEqual(high_card(hand2, hand1), -1)
        self.assertEqual(high_card(hand1, hand1), 0)

        hand1 = parse_hand("5H 5C 6S 7S KD")
        hand2 = parse_hand("2C 3S 8S 8D TD")
        self.assertEqual(one_pair(hand1, hand2), -1)
        self.assertEqual(one_pair(hand2, hand1), 1)
        self.assertEqual(one_pair(hand2, hand2), 0)
        hand1 = parse_hand("4D 6S 9H QH QC")
        hand2 = parse_hand("3D 6D 7H QD QS")
        #self.assertEqual(one_pair(hand1, hand2), 1)
        #self.assertEqual(one_pair(hand2, hand1), -1)
        #self.assertEqual(one_pair(hand1, hand1), 0)
        hand1 = parse_hand("2D 2C 3D 3C AS")
        hand2 = parse_hand("2C 3C 4C 5C KC")
        self.assertEqual(two_pairs(hand1, hand2), 1)
        self.assertEqual(two_pairs(hand2, hand1), -1)
        self.assertEqual(two_pairs(hand1, hand1), 0)
        hand1 = parse_hand("2D 2C 4D 4C AS")
        hand2 = parse_hand("3D 3C 4H 4S KS")
        self.assertEqual(two_pairs(hand1, hand2), -1)
        self.assertEqual(two_pairs(hand2, hand1), 1)
        self.assertEqual(two_pairs(hand1, hand1), 0)
        hand1 = parse_hand("2D 2C 2S 3D AS")
        hand2 = parse_hand("2D 2D 3D 3C KS")
        self.assertEqual(three_of_a_kind(hand1, hand2), 1)
        self.assertEqual(three_of_a_kind(hand2, hand1), -1)
        self.assertEqual(three_of_a_kind(hand1, hand1), 0)
        hand2 = parse_hand("3D 3C 3S 4S 5S")
        self.assertEqual(three_of_a_kind(hand1, hand2), -1)
        self.assertEqual(three_of_a_kind(hand2, hand1), 1)
        self.assertEqual(three_of_a_kind(hand2, hand2), 0)
        hand1 = parse_hand("2D 3D 4D 5D 6D")
        hand2 = parse_hand("2D 3D 4D 5D AS")
        self.assertEqual(straight(hand1, hand2), 1)
        self.assertEqual(straight(hand2, hand1), -1)
        self.assertEqual(straight(hand1, hand1), 0)
        hand2 = parse_hand("3D 4D 5D 6D 7D")
        self.assertEqual(straight(hand1, hand2), -1)
        self.assertEqual(straight(hand2, hand1), 1)
        self.assertEqual(straight(hand2, hand2), 0)
        
        # second hand wins, because it has a higher card
        #self.assertEqual(flush(hand1, hand2), -1)
        #self.assertEqual(flush(hand2, hand1), 1)
        #self.assertEqual(flush(hand2, hand2), 0)
        hand2 = parse_hand("2D 3D 4D 5D 6C")
        self.assertEqual(flush(hand1, hand2), 1)
        self.assertEqual(flush(hand2, hand1), -1)
        self.assertEqual(flush(hand1, hand1), 0)
        hand1 = parse_hand("2C 2D 2S 3C 3D")
        hand2 = parse_hand("2C 2D 3C 3D 4D")
        self.assertEqual(full_house(hand1, hand2), 1)
        self.assertEqual(full_house(hand2, hand1), -1)
        self.assertEqual(full_house(hand1, hand1), 0)
        hand2 = parse_hand("2C 2D 2S 4C 4D")
        self.assertEqual(full_house(hand1, hand2), -1)
        self.assertEqual(full_house(hand2, hand1), 1)
        self.assertEqual(full_house(hand2, hand2), 0)
        hand2 = parse_hand("3C 3D 3S 2C 2D")
        self.assertEqual(full_house(hand1, hand2), -1)
        self.assertEqual(full_house(hand2, hand1), 1)
        self.assertEqual(full_house(hand2, hand2), 0)
        hand1 = parse_hand("2C 2D 2H 2S 3C")
        hand2 = parse_hand("4C 4D 4H 5C 5D")
        self.assertEqual(four_of_a_kind(hand1, hand2), 1)
        self.assertEqual(four_of_a_kind(hand2, hand1), -1)
        self.assertEqual(four_of_a_kind(hand1, hand1), 0)
        
        self.assertEqual(straight_flush(hand1, hand2), 0)
        hand1 = parse_hand("2C 3C 4C 5C 6C")
        hand2 = parse_hand("2D 3D 4D 5D 7D")
        self.assertEqual(straight_flush(hand1, hand2), 1)
        self.assertEqual(straight_flush(hand2, hand1), -1)
        hand2 = parse_hand("2D 3D 4D 5D 6C")
        self.assertEqual(straight_flush(hand1, hand2), 1)
        self.assertEqual(straight_flush(hand2, hand1), -1)

        hand1 = parse_hand("2C 2D 3C 5C 6C")
        hand2 = parse_hand("2H 2S 3C 5C 7C")
        self.assertEqual(decide_winner(hand1, hand2), -1)
        self.assertEqual(decide_winner(hand2, hand1), 1)
        hand1 = parse_hand("2C 2D 3C 3D 6C")
        self.assertEqual(decide_winner(hand1, hand2), 1)
        self.assertEqual(decide_winner(hand2, hand1), -1)
        hand2 = parse_hand("3C 3D 4C 5D 6C")
        self.assertEqual(decide_winner(hand1, hand2), 1)
        self.assertEqual(decide_winner(hand2, hand1), -1)
        hand1 = parse_hand("2C 2D 4S 5S 6S")
        self.assertEqual(decide_winner(hand1, hand2), -1)
        self.assertEqual(decide_winner(hand2, hand1), 1)

    def test0055(self):
        from id_0055 import is_Lychrel_below_1000

        self.assertEqual(is_Lychrel_below_1000(47), False)
        self.assertEqual(is_Lychrel_below_1000(349), False)

    def test0058(self):
        from id_0058 import spiral_vertices

        v = [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
        f = spiral_vertices()
        x = 0
        for n in range(len(v)):
            self.assertEqual(f.next(), v[x])
            x += 1

    def test0059(self):
        from id_0059 import xor_encrypt

        key = "abc"
        message = "This is a secret message"
        enc = xor_encrypt(message, key)
        self.assertEqual(xor_encrypt(enc, key), message)
        
    def test0061(self):
        from id_0061 import is_cyclic, find_cyclic_nums

        self.assertEqual(is_cyclic([8128, 2882, 8281]), True)
        self.assertEqual(is_cyclic([8128, 2882, 8282]), False)
        self.assertEqual(is_cyclic([8128, 2982, 8281]), False)
        f = find_cyclic_nums([[1011], [1123, 1223], [2310]])
        self.assertEqual(f.next(), [1011, 1123, 2310])

    def test0062(self):
        from id_0062 import is_permutation

        self.assertEqual(is_permutation(123456789, 987654321), True)
        self.assertEqual(is_permutation(123456, 123457), False)

    def test0064(self):
        from id_0064 import continued_fraction_sqrt

        sqrt2 = [1, 2, 2, 2]
        f = continued_fraction_sqrt(2)
        for i in range(len(sqrt2)):
            r = f.next()
            self.assertEqual(r, sqrt2[i])
        sqrt7 = [2, 1, 1, 1, 4, 1, 1, 1, 4]
        f = continued_fraction_sqrt(7)
        for i in range(len(sqrt7)):
            r = f.next()
            self.assertEqual(r, sqrt7[i])

    def test0066(self):
        from id_0066 import solves_equation

        self.assertEqual(solves_equation(649, 180, 13), True)
        self.assertEqual(solves_equation(3, 2, 2), True)
        self.assertEqual(solves_equation(3, 1, 2), False)

    def test0068(self):
        from id_0068 import check_sums, fill_n_gon, make_num_from_lst

        lst = fill_n_gon([4, 6, 5, 2, 1, 3])
        #print lst
        self.assertEqual(check_sums(lst), True)
        self.assertEqual(make_num_from_lst(lst), 432621513)

    def test0069(self):
        from id_0069 import totient, totient2

        self.assertEqual(totient(9), 6)
        for n in range(3, 100):
            self.assertEqual(totient(n), totient2(n))

    def test0076(self):
        from id_0076 import sums, Sums

        self.assertEqual(sums(5), 6)
        self.assertEqual(sums(6), 10)
        self.assertEqual(Sums(6), sums(6))
        self.assertEqual(Sums(5), sums(5))
        self.assertEqual(Sums(10), sums(10))

    def test0077(self):
        from id_0077 import sums, new_sums

        for n in range(4, 15):
            self.assertEqual(sums(n), new_sums(n))

    def test0078(self):
        from id_0076 import Sums
        from id_0078 import P

        for n in range(1, 50):
            self.assertEqual(Sums(n) + 1, P(n))

    def test0081(self):
        from id_0081 import solve

        self.assertEqual(2427, solve('id_0081-test.txt'))

    def test0082(self):
        from id_0082 import solve

        self.assertEqual(994, solve('id_0082-test.txt'))

    def test0085(self):
        from id_0085 import rect

        self.assertEqual(18, rect(3, 2))

    def test0201(self):
        from id_0201 import U, U2

        #self.assertEqual(sum(U([1, 3, 6, 8, 10, 11], 3)), 156)
        #self.assertEqual(U2([1, 2, 3], 2), 12)
        #self.assertEqual(U2([1, 3, 6, 8, 10, 11], 3), 156)

    def test0113(self):
        from id_0113 import increasing

        self.assertEqual(45, increasing(2, 1))
        for n in range(2, 5):
            r = increasing(n, 1)
            s = 0
            for k in range(1, 10):
                s += increasing(n - 1, k)
            self.assertEqual(r, s)

if __name__ == '__main__':
    unittest.main()
