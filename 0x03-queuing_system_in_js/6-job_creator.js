// create a queue with kue
// create a job with the queue

const kue = require('kue');

const queue = kue.createQueue();

const data = {
  phoneNumber: '918-555-5555',
  message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', data).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log(`Notification job ${job.id} completed`);
});

job.on('failed', () => {
  console.log(`Notification job ${job.id} failed`);
});
