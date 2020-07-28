## HMM and Vertibi algorithm  维特比预测问题算法
import numpy as np
def Viterbi(A, B, PI, Q, V, obs):
	N = len(Q)
	T = len(obs)
	delta = np.array([[0]*N]*T, dtype=np.float64)
	phi = np.array([[0]*N]*T, dtype=np.int64)
	# print(delta,phi)

	## init
	for i in range(N):
		delta[0,i] = PI[i]*B[i][V.index(obs[0])] # 第一天在三个地方不购物的概率
		phi[0,i] = 0

	# print(delta, phi)

	for i in range(1, T): # 分别对应 不购物，购物，购物
		for j in range(N): # 分别对应三个地点
			tmp = [delta[i-1, k]*A[k][j] for k in range(N)]  # 此时tmp是状态转移后出现在每个地点的概率
			# print(tmp)
			delta[i,j] = max(tmp) * B[j][V.index(obs[i])]  # 出现在该地点且出现obs中状态的最大概率
			phi[i,j] = tmp.index(max(tmp)) # 记录最大概率对应的地点
	# print(delta)
	# print(phi)
	P = max(delta[T-1,:])
	I = int(np.argmax(delta[T-1,:]))
	path = [I]
	for i in reversed(range(1,T)):
		end = path[-1]
		path.append(phi[i, end])

	hidden_stats = [Q[i] for i in reversed(path)]
	return P, hidden_stats

def main():
	# state
	Q = ["欢乐谷", "迪士尼", "外滩"]
	# observation
	V = ["购物", "不购物"]
	# 转移概率矩阵 Q -> Q  第一天在欢乐谷第二天还在欢乐谷的概率是0.8
	A = [[0.8, 0.05, 0.15],
	     [0.2, 0.6, 0.2],
	     [0.2, 0.3, 0.5]]
	# 发射概率矩阵 Q -> V  去欢乐谷购物的概率是0.1, 不购物的概率是0.9
	B = [[0.1, 0.9],
	     [0.8, 0.2],
	     [0.3, 0.7]]
	# 初始概率
	PI = [1/3, 1/3, 1/3]
	# 观测序列
	obs = ["不购物", "购物", "购物"]

	P,hidden_states = Viterbi(A,B,PI,Q,V,obs)

	print('最大的概率为: %.5f' % P)
	print('隐藏序列为：%s' % hidden_states)

if __name__ == '__main__':
    main()