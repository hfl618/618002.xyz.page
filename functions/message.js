export async function onRequestPost(context) {
  const data = await context.request.json();
  // 这里可以把 data 存入 D1 数据库
  return new Response("收到了！内容是：" + data.content);
}