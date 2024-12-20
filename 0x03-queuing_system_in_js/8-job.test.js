// test jobs

import kue from 'kue';

import createPushNotificationJobs from './8-job.js';

const mocha = require('mocha');

const expect = require('chai').expect;

const queue = kue.createQueue();

const Jobs = [
  { phoneNumber: '9185550000', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550001', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550002', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550003', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550004', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550005', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550006', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550007', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550008', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '9185550009', message: 'This is the code 1234 to verify your account' },
];

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('createPushNotificationJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationJobs('string', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('show show the count of jobs in Jobs', () => {
    createPushNotificationJobs(Jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(10);
  });
});
