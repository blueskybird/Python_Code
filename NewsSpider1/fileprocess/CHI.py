# -*- coding: utf-8 -*-
import os

class CHI:

    def __init__(self):
        self.constellation = {}
        self.constellation_len = 0
        self.economic = {}
        self.economic_len = 0
        self.food = {}
        self.food_len = 0
        self.health = {}
        self.health_len = 0
        self.sport = {}
        self.sport_len = 0
        self.tecnology = {}
        self.tecnology_len = 0
        self.travel = {}
        self.travel_len = 0

        self.allfeatures = {}


    def category_filepath(self):
        '''
        获得单个类别特征项统计的文件的路径
        :return:
        '''
        file_dir = r'F:\wordNum\xinlangweibowordnum'
        filenames = os.listdir(file_dir)
        file_paths = []

        for filename in filenames:
            file_paths.append(os.path.join(file_dir,filename))

        return file_paths


    def read_file(self, path):
        f = open(path, 'r')
        line = f.readline()
        dic = {}
        while line:
            line_split = line.strip().split(' ')
            val = []
            for i in line_split[1:]:
                val.append(int(i))
            dic[line_split[0]] = val
            line = f.readline()
        f.close()
        return dic


    def get_category_vec(self, file_paths):

        for i in range(len(file_paths)):
            if i == 0:
                self.constellation = self.read_file(file_paths[i])
                for k, v in self.constellation.iteritems():
                    self.constellation_len = v[0] + v[2]
                # print self.constellation_len
            elif i == 1:
                self.economic = self.read_file(file_paths[i])
                for k, v in self.economic.iteritems():
                    self.economic_len = v[0] + v[2]
                # print self.economic_len
            elif i == 2:
                self.food = self.read_file(file_paths[i])
                for k, v in self.food.iteritems():
                    self.food_len = v[0] + v[2]
                # print self.food_len
            elif i == 3:
                self.health = self.read_file(file_paths[i])
                for k, v in self.health.iteritems():
                    self.health_len = v[0] + v[2]
                # print self.health_len
            elif i == 4:
                self.sport = self.read_file(file_paths[i])
                for k, v in self.sport.iteritems():
                    self.sport_len = v[0] + v[2]
                # print self.sport_len
            elif i == 5:
                self.tecnology = self.read_file(file_paths[i])
                for k, v in self.tecnology.iteritems():
                    self.tecnology_len = v[0] + v[2]
                # print self.tecnology_len
            elif i == 6:
                self.travel = self.read_file(file_paths[i])
                for k, v in self.travel.iteritems():
                    self.travel_len = v[0] + v[2]
                # print self.travel_len


    def merge_category_vec(self):
        ls = []
        ls.append(self.constellation)
        ls.append(self.economic)
        ls.append(self.food)
        ls.append(self.health)
        ls.append(self.sport)
        ls.append(self.tecnology)
        ls.append(self.travel)

        ls_len = []
        ls_len.append(self.constellation_len)
        ls_len.append(self.economic_len)
        ls_len.append(self.food_len)
        ls_len.append(self.health_len)
        ls_len.append(self.sport_len)
        ls_len.append(self.tecnology_len)
        ls_len.append(self.travel_len)

        for i in range(len(ls)):
            for j in range(len(ls)):
                if i == j:
                    continue
                # print i, j
                for k in ls[i]:
                    if ls[j].has_key(k):
                        ls[i][k][1] += ls[j][k][0]
                        ls[i][k][3] += ls[j][k][2]
                    else:
                        ls[i][k][3] += ls_len[j]

        filenames = []
        filenames.append('constellation')
        filenames.append('economic')
        filenames.append('food')
        filenames.append('health')
        filenames.append('sport')
        filenames.append('tecnology')
        filenames.append('travel')

        #将特征项写到对应的文本中
        for i in range(len(filenames)):
            f = open(r'F:\wordNum\xinlangweibowordnum_zuizhong\\'+filenames[i]+'.txt', 'w')
            for k, v in ls[i].iteritems():
                f.write(k + ' ')
                for j in v:
                    f.write(str(j) + ' ')
                f.write('\n')
            f.close()

    def calculate_and_write_to_file(self):
        '''
        将最终计算结果写入文件
        :return:
        '''
        ls = []
        ls.append(self.constellation)
        ls.append(self.economic)
        ls.append(self.food)
        ls.append(self.health)
        ls.append(self.sport)
        ls.append(self.tecnology)
        ls.append(self.travel)

        N = self.constellation_len + self.economic_len + self.food_len + self.health_len + self.sport_len + self.tecnology_len + self.travel_len

        for i in range(len(ls)):
            for k, v in ls[i].iteritems():
                A = v[0]
                B = v[1]
                C = v[2]
                D = v[3]
                n = v[4]

                chi_val = 0

                a = float(n)/(float(A) + float(C))

                if A*D - B*C <= 0:
                    chi_val = 0
                else:
                    # fenzi = float(N) * (float(A)*float(D) - float(B)*float(C)) * (float(A)*float(D) - float(B)*float(C))
                    fenzi = N * (A*D - B*C ) * (A*D - B*C )
                    fenmu = (A+C)*(B+D)*(A+B)*(C+D)
                    chi_val = float(fenzi)/float(fenmu)*a


                if self.allfeatures.has_key(k):
                    if self.allfeatures[k] < chi_val:
                        self.allfeatures[k] = chi_val
                else:
                    self.allfeatures[k] = chi_val

        f = open(r'F:\wordNum\xinlangweibofeatures.txt', 'w')
        print 'the number of feature is ' , len(self.allfeatures)
        for k, v in self.allfeatures.iteritems():
            # if v > 0:
            if v > 0.008:
                f.write(k+ ' ' + str(v))
                f.write('\n')
        f.close()




if __name__ == '__main__':
    chi = CHI()
    file_paths = chi.category_filepath()
    chi.get_category_vec(file_paths)
    chi.merge_category_vec()
    chi.calculate_and_write_to_file()