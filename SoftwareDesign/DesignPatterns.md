# 设计模式

>设计模式 | C++ | 目前就两个

## 一、简单工厂模式
由工厂类提供接口，根据不同的入参构造不同的Operate派生类，并返回统一的基类，使得客户端的调用与每个派生类的具体实现隔离开。扩展Operate只需要新增一个Operate派生类，不过仍然需要修改工厂类。

```C++
class Factory
{
    public static Operate create(char oper)
    {
        Operate operate = null;
        switch(oper)
        {
            case 'A':
                operate = new OperateA();
                break;
            //...
        }
        return operate;
    }
}
class Operate
{
    public virtual void func();
}
class OperateA : Operate
{
    public void func();
}
class OperateB : Operate
{
    public void func();
}
//...
```
## 二、策略模式

>\[DP]: 它定义了算法家族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化，不会影响到使用算法的客户。

利用Context类，可以构造不同的策略。统一调用的func接口，包装了不同策略的func实现细节。
```C++
class Context   // 上下文类
{
    Strategy st;
    public Context(Strategy st)
    {
        this.st = st;
    }
    public void func_interface
    {
        st.func();
    }
}
class Strategy  // 策略基类
{
    public virtual void func();
}
class StrategyA : Strategy  // 策略派生类
{
    public void func();
}
class StrategyB : Strategy  // 策略派生类
{
    public void func();
}
```
将策略模式与简单工厂结合，Context的构造函数中不是传入策略类，而是一个可以表示策略类型的值（如字符串）,然后由Context再去构造相应的策略。这样，客户端仅需要与Context类打交道即可以使用不同的策略。

## 三、装饰模式
>\[DP]: 动态地给一个对象添加一些额外的职责，就增加功能来说，装饰模式比生成子类更为灵活。



