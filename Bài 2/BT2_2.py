# class LineSegmentTest:

#     def testCase(self):

#         # đọc dữ liệu
#         x1, y1, x2, y2 = map(int, input().split())

#         # tạo đoạn thẳng
#         ls1 = LineSegment(x1, y1, x2, y2)

#         # in thông tin
#         ls1.print()
#         print(round(ls1.length(), 1))
#         print(ls1.angle())

#         # copy sâu
#         ls2 = LineSegment(ls1)

#         # di chuyển ls1
#         ls1.move(1, 1)

#         # in kết quả
#         ls1.print()
#         ls2.print()