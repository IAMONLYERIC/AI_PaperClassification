import requests
from bs4 import BeautifulSoup


# with open('nips2019_paper.html','rb') as f:
#     text = f.read()
def get_write_file():
    re = requests.session()
    r = re.get(r'https://nips.cc/Conferences/2019/AcceptedPapersInitial')
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    paper_div = soup.find_all(class_='col-xs-9')[1]
    paper_list = list(paper_div.find_all('b'))
    paper_list = [str(x).lstrip('<b>').rstrip('</b>') for x in paper_list]

    with open('nips2019_paper_name.txt','wb') as f:
        for name in paper_list:
            f.write(bytes(name,'utf-8') + bytes('\n','utf-8'))


def classify_paper():

    class_dict = {'检测类':['Detection','Detect',], # 物体检测，异常检测，三维物体检测
                  '分割类' : ['Segmentation', ], # 分割相关 语义分割 实例分割 物体分割
                  '分类识别' : ['Classification', 'Recognition'], # 分类 识别
                  '姿态' : ['Pose'], # 姿态估计
                  '跟踪' : ['Track', 'Tracking'], # 目标跟踪
                  '视频相关' : ['Video'], # 视频
                  '强化学习' : ['Reinforcement', 'Reinforce', 'Reinforcing'], # 强化学习
                  '超分辨率' : ['Super-resolution', 'Super Resolution', 'Resolution'],  # 超分辨率
                  '3D点云重建类' : ['3D', 'Point Cloud', 'Reconstruction'], # 3D 点云 重建
                  '生成模型' : ['GAN', 'Generative','Generation','Generating','autoencoders','Auto-Encoder','VAE'], # Gan 生成模型  对抗
                  'few_shot' : ['Few-shot', 'One-shot', 'Meta-Learning','Zero-shot'], # few-shot one-shot 小样本学习 元学习
                  '语言文字处理' : ['Text', 'Language'], # 文本 语言处理
                  '机器学习' : ['Bayes', 'Bayesian', 'tree', 'optimization','Machine Learning',
                          'Metric Learning','Low-Rank','Low Rank','gaussian process','Regression',
                          'Flow','Markov','boosting','bagging','Monte','Distribution','Cluster',
                          ], # 机器学习  优化
                  '可解释性' : ['Interpretable', 'Interpretability', 'Interpretation', 'Explanations'], # 可解释学习
                  '表征表示':['Representation'], # 表征 表示
                  '数据集与benchmark':['Benchmark','Dateset']   ,# 数据集、Benchmark
                  'embedding':['Embedding'], # 嵌入
                  '注意力模型':['Attention'], # 注意力模型
                  '去噪':['denoising','denoise','Denoisers'] ,# 去噪
                  '与网络相关的':['Net','Network','CNN','RNN'], # 与网络相关的论文
                  '与网络架构相关的':['Architecture','NAS'],  # 网络架构  架构搜索
                  '非监督半监督学习':['unsupervised','Semi-Supervised'], # 非监督学习 半监督学习
                  '图相关':['graph','GNN'], # 图相关
                  '对抗攻击相关':['Adversarial','Attack'], # 对抗相关
                  '模型剪枝压缩':['Pruning','compression','compress'] # 模型压缩
                  }

    for cate in class_dict.keys():
        keywords_list = class_dict.get(cate)
        # 读取论文名称到列表中
        with open('nips2019_paper_name.txt','r') as f1:
            paper_name_list = f1.readlines()
            paper_name_list = [x[0:-1] for x in paper_name_list]
        with open('./nips2019_results/' + str(cate)+'.txt','w') as f2:
            for index,paper_name in enumerate(paper_name_list):
                flag = False
                for keyword in keywords_list:
                    if paper_name.lower().find(keyword.lower()) >= 0:
                        flag = True
                if flag == True:
                    f2.write(paper_name+'\n')
                    paper_name_list[index] = paper_name + '  OOO'
        print('cate : '+ str(cate) + ' is done!\n')

        with open('nips2019_paper_name.txt','w') as f:
            for name in paper_name_list:
                f.write(name +'\n')


def count_classified_papers():

    counts = 0
    non_used_paper = []
    with open('nips2019_paper_name.txt', 'r') as f1:
        paper_name_list = f1.readlines()
        paper_name_list = [x[0:-1] for x in paper_name_list]
        # print(paper_name_list)
        for name in paper_name_list:
            if name.endswith('OOO'):
                counts += 1
            else:
                non_used_paper.append(name)
    with open('no_used_paper.txt','w') as f2:
        for name in non_used_paper:
            f2.write(name + '\n')
    print(counts)



if __name__ == '__main__':
    get_write_file()
    classify_paper()
    count_classified_papers()



