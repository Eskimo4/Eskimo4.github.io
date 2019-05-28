# 排序

> 升序 | C++

## 各个排序算法的性能分析

命令 | 描述
-|-

算法 | 最坏时间复杂度 | 最好时间复杂度 | 平均时间复杂度 | 空间复杂度 | 是否稳定 | 1W规模的排序时间（ms）
-|-|-|-|-|-|-
冒泡 | O(n<sup>2</sup>) | O(n) | O(n<sup>2</sup>) | O(1) | 稳定 | 34430
选择 | O(n<sup>2</sup>) | O(n<sup>2</sup>) | O(n<sup>2</sup>) | O(1) | 不稳定 | 19250
插入 | O(n<sup>2</sup>) | O(n) | O(n<sup>2</sup>) | O(1) | 稳定 | 10349
希尔 | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | 稳定 | 99
快速 | O(n<sup>2</sup>) | O(nlogn) | O(nlogn)| O(logn) | 不稳定 | 93
堆   | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | 不稳定| 135
归并 | O(nlogn) | O(nlogn) | O(nlogn) |O(n) | 稳定 | 144

## 一、冒泡排序
冒泡排序是一种最简单的排序算法，逐次比较相邻两个元素的大小，把较大的放在后面。每次循环结束就可以在未排序区得到一个最大值放在最后面，n次循环结束后排序即完成。

```C++
void Bubble(vector<int>& v, int begin, int end)
{
	int size = v.size();
	for (int i = 0; i < size; i++)
	{
		bool swap = false;
		for (int j = 0; j < size - i - 1; j++)
		{
			if (v[j] > v[j + 1])
			{
				int tmp = v[j];
				v[j] = v[j + 1];
				v[j + 1] = tmp;
				swap = true;
			}
		}
		if (!swap)
			break;
	}
}
```
通过判断每趟冒泡是否有交换操作，可在**未排序区**已排好序的情况下提前结束，使得算法的最好时间复杂度为O(n)。

## 二、选择排序
选择排序的思想是，每次在未排序区选择一个最小值放在已排序区的末尾。

```C++
void Select(vector<int>& v, int begin, int end)
{
	for (int i = begin; i < end; i++)
	{
		int index = i;
		for (int j = i; j <= end; j++)
		{
			if (v[j] < v[index])
				index = j;
		}
		int tmp = v[i];
		v[i] = v[index];
		v[index] = tmp;
	}
}
```
## 三、插入排序
每次循环，将未排序区的第一个数插入到已排序区。从已排序区的末尾向前遍历，逐个比较，找到插入的位置即可。
```C++
void Insert(vector<int>& v, int begin, int end)
{
	for (int i = begin + 1; i <= end; i++)
	{
		int cur = v[i];
		int pos = i - 1;
		for (; pos >= begin && v[pos] > cur; pos--)
			v[pos + 1] = v[pos];
		v[pos + 1] = cur;
	}
}
```
## 四、希尔排序

希尔排序是一种改进的插入排序，它会优先比较距离较远的元素，也称为缩小增量排序。希尔排序是把数组按一定增量分组，分别对每个组进行插入排序。然后增量逐渐减小，再重复分组和排序。直到增量为1后，整个数组即排序完成。

```C++
void Hill(vector<int>& v, int begin, int end)
{
	int len = v.size() / 2;		// 增量初始值设为总长度的一半
	while (len)
	{
		for (int offset = 0; offset < len; offset++)
		{
			for (int i = begin + offset + len; i <= end; i += len)
			{
				int cur = v[i];
				int pos = i - len;
				for (; pos >= begin + offset && v[pos] > cur; pos -= len)
					v[pos + len] = v[pos];
				v[pos + len] = cur;
			}
		}
		len /= 2;	// 下次循环增量减半
	}
}
```

## 五、快速排序
快速排序是一种递归算法，故而其空间复杂度为O(logn)。

快排的原理：选择一个基准值，通过一趟排序，将数组分为两部分，小于基准值和大于基准值的。然后分别对两个部分递归排序。
```C++
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
可以用随机选择基准值替代以begin为基准值，可以防止在数组已经有序的情况下快排退化为冒泡。

可以使用尾递归来减少递归运算时所消耗的栈空间。

## 六、堆排序
堆排序利用完全二叉树的数据结构，在待排序数组中建立最大堆，以达到每次循环得到未排序区的最大值的目的。

首先在在数组中初始化一个最大堆，然后进行循环。每次循环中，将根节点的值（即第一个元素）和未排序区的最后一个值互换，再从根节点向下调整最大堆，未排序区的个数减一。

```C++
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
void HeapSort(vector<int>& v, int begin, int end)
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

## 七、归并排序
归并排序采用了分治法的思想，将待排序数组分为两部分，对每一部分进行归并排序，然后将两个排好序的数组合并。
```C++
vector<int> tmp;
void Merge(vector<int>& v, int begin, int end)
{
	if (end <= begin)
		return;
	int mid = begin + (end - begin) / 2;
	Merge(v, begin, mid);
	Merge(v, mid + 1, end);

	tmp.resize(v.size());
	for (int i = begin, j = mid + 1, k = begin; k <= end;)
	{
		while (i == mid + 1 && k <= end)
			tmp[k++] = v[j++];
		while (j == end + 1 && k <= end)
			tmp[k++] = v[i++];
		if (k > end)
			break;
		if (v[i] > v[j])
			tmp[k++] = v[j++];
		else
			tmp[k++] = v[i++];
	}
	for (int i = begin; i <= end; i++)
		v[i] = tmp[i];
}
```

## 八、计数排序
计数排序的算法思想很简单，而且只能用于取值范围有限的整数数组的排序。
创建一个统计数组，然后遍历待排序数组，将每个元素出现的次数加起来，存放到统计数组中元素值对应的下标上。

```C++
//TODO
```