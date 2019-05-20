# 排序

> 升序 | C++

## 一、冒泡排序

时间复杂度：O(n<sup>2</sup>)

空间复杂度：O(1)

稳定

```C++
#include <vector>
using namespace std;

void Bubble(vector<int>& v)
{
	int size = v.size();
	for(int i=0;i<size;i++)
		for (int j = 0; j < size - i - 1; j++)
		{
			if (v[j] > v[j + 1])
			{
				int tmp = v[j];
				v[j] = v[j + 1];
				v[j + 1] = tmp;
			}
		}
}
```

## 二、堆排序

时间复杂度：O(nlogn)

空间复杂度：O(1)

不稳定

```C++
#include <vector>
using namespace std;

void adjust(vector<int>& v, int cur, int n)
{
	int tmp = v[cur];
	int k;
	while ((k = 2 * cur + 1) < n)
	{
		if (k + 1 < n && v[k + 1] > v[k])
			k++;
		if (v[k] > tmp)
		{
			v[cur] = v[k];
			cur = k;
		}
		else
			break;
	}
	v[cur] = tmp;
}
void HeapSort(vector<int>& v)
{
	if (v.size() < 2)
		return;
	for (int i = v.size() / 2 - 1; i >= 0; i--)
		adjust(v, i, v.size());
	/*cout << "初次构造的最大堆：" << endl;
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << "\t";
	cout << endl;*/
	for (int i = v.size() - 1; i > 0; i--)
	{
		{
			int tmp = v[0];
			v[0] = v[i];
			v[i] = tmp;
		}
		adjust(v, 0, i);
	}
}
```

## 3、快速排序

最坏时间复杂度：O(n<sup>2</sup>)
平均时间复杂度：O(nlogn）
空间复杂度：O(1)

```C++
#include <vector>
using namespace std;

void Quick(vector<int>& v,int begin,int end)
{
	if (begin >= end)
		return;
	int tmp = v[begin];
	int i = begin, j = end;
	while (i < j)
	{
		while (v[j] >= tmp && j > i)
			j--;
		v[i] = v[j];
		while (v[i] < tmp && i < j)
			i++;
		v[j] = v[i];
	}
	v[i] = tmp;
	Quick(v, begin, i - 1);
	Quick(v, i + 1, end);
}
```

可以用随机选择基准值替代以begin为基准值，可以防止在有序情况下快排退化为冒泡。
可以使用尾递归来减少递归运算时所消耗的栈空间。