* enum -> 大概是包含同种类不同东西的集合，写出来之后可以在后面直接调用
* c#的继承没有多重继承，继承的类调用基类的用base
* get only：为了一些不会改变的东西，比如血量（保持save，避免一些愚蠢操作）
```
class Player
{
	private int _health = 100;
	public int health
	{
		get
		{
			return _health;
		}
		//通过这行set可以通过一些奇怪的操作改变这个值
		set
		{
			if(value <= 0){
				_health = 0;
			}
			else if (value >= 100){
				_health = 100;
			}
			else{
			_health = value;
		}
		}
	}
}
```
这样既可以访问，还可以保持这个值不会改变。后面这种set的方式，比如摔下悬崖掉200点血，但是血只会清零
* intrface：里面需要定义属性的data type和方法，比如定义一个interface的名字是iitem
	* claas Sword : iitem
	* 可以从不同的interface里面继承
	* 可以继承不同的interface（爽到）
	* 在interface的定义里面不用写具体的method
	* 这样写起代码来不同属性的东西继承了同一个interface代码可以快乐粘贴
	* 最牛逼的方法出现了，这个方法可以筛选这个对象有没有这个interface
```
//假设有两个interface：IItem和IPartOfQuest。两个对象sword（有partofquest）和axe（没有）

IItem[] inventory = new IItem[2];
inventory[0] = sword;
inventory[1] = axe;

for (int = 0; i < inventory.Length; i++){
	//axe没有就会返回null
	IPartOfQuest questItem = inventory[i] as IPartOfQuest;
	if (questItem != null){
		//call the functon in partofquest
	}
}
```

* generics
	* 当我们不知道object的类型的时候
	* 写在尖括号里，可以在后面调用的时候再定义类型