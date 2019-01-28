* start:创建对象时候调用的函数，类似java里面的构造函数
* update（）：对对象更新时调用的函数（每一帧都会调用），根据渲染的帧数调用
	* fixedupdate：采用真实的间隔作为帧长，**处理物理逻辑**
* rigidbody：
	* 给小球绑定一个刚体对象，小球可以被物理引擎控制
	* 需要通过刚体实现重力，交互，或者施加的力
	* addforce给小球增加移动（储存在三维数组里面）
* input
	* 可以获取到控制器的操作属性（键盘，手柄，触摸板）
	* getaxis，得到两个方向的饿意动
* 相机移动
	* 使用transform获得初始状态的相机的位置和player的位置
	* 做差，求相对位置
	* 在每次的update中，通过把物体的位置加上相对位置得到相机的位置
	* 注：**不把相机放在物体的子项是因为物体是个球，这样相机会转，要是物体不是个球的话没有问题**
* transform.rotate -> 控制物体旋转（乘一个时间常数time.deltaTime就可以随时间旋转）
* OnTriggerEnter（Collider other），检测碰撞，如果碰撞物体的tag是string里面的值，则把active设置为false
	* Triggers are a special type of collider. They make an object intangible, so it looks like it can’t touch other objects. 
	